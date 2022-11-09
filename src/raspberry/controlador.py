from .utiles.getDateCurrent import getDate_Current
import RPi.GPIO as GPIO
from .database.operaciones import Asientosdisponibles, existeRegistrosFechaActual,ingresarRegistroPasajeros,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft,getDatosActuales,getRoutes
from .database.conexion import create_connection,main,isSqlite3Db
from .serial.sendData import sendDatabySerial,sendDatabySerial2,getred,sendred
from .serial.sensorica import sensorica #sensorica2
import os
from dotenv import load_dotenv
from os.path import join, dirname
from .vista.MostrarDatos import agregar





def controladorIngreso():
    #if(controladorSensorIngreso):
        if( isSqlite3Db() ): 
            conn = create_connection()
        else:
            conn = main()
        dateCurrent = getDate_Current()
        if( existeRegistrosFechaActual( conn , dateCurrent)  ):
            if( disponibilidadBus( conn , dateCurrent ) ):
                actualizarRegistroSuma( conn , dateCurrent )
                ingreso="Ingeso Pasajeros"
            else:
                bloqueo="Bloqueo de puerta"
                print(bloqueo)
        
            #print(Bloq)
        else:
            """ Enviar al arduino """
            ingresarRegistroPasajeros( conn , dateCurrent )
            A="Ingreso al inicio del dia"
            print(A)

        Ing=getDatosActuales(conn,dateCurrent)
        agregar(Ing)
        enarduin=str(Ing[1])
        sendDatabySerial(enarduin)
        print(enarduin)

def controladorSalida():
    #if(controladorSensorSalida()):
        if( isSqlite3Db() ): 
            conn = create_connection()
            dateCurrent = getDate_Current()
            if( existeRegistrosFechaActual( conn , dateCurrent )):
                if( validateLeft( conn , dateCurrent )):
                    data=getred()
                    if(data=="restar"):
                        actualizarRegistroResta( conn , dateCurrent )
                        """ Actualizar y enviar al arduino"""
                        B="Ingreso un pasajeros"
                    
                        print(B)               
                else:
                    print("Enviar al arduino ")   

        Sal=(getDatosActuales(conn,dateCurrent))
        agregar(Sal)
        salard=str(Sal[1])
        sendred(salard)
        #sendDatabySerial2(salard)
        print(salard)
    

def controladorDatos():
    datospantalla=[]
    if( isSqlite3Db() ): 
        conn = create_connection()
        dateCurrent = getDate_Current()
        datospantalla=(getDatosActuales(conn,dateCurrent))
        print(datospantalla)
    return datospantalla



def SendData(conn,dateCurrent):
    des1=(getRoutes(conn))  
    print(des1)
    Sal=(getDatosActuales(conn,dateCurrent))
    salard=str(Sal[1])
    sendDatabySerial(salard)
    print(salard)
    return Sal

def controladorSensorIngreso():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    TRIGH = os.environ.get("TRIGH")
    ECHO = os.environ.get("ECHO")
    distanciaS1=(sensorica(TRIGH,ECHO))
    if(distanciaS1):
        n=True
        return n
    GPIO.cleanup()

def controladorSensorSalida():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    TRIGH1 = os.environ.get("TRIGH1")
    ECHO1 = os.environ.get("ECHO1")
  
    distanciaS2=(sensorica(TRIGH1,ECHO1))
    if(distanciaS2):#aqui calibramos al sensor
        n=True
        return n
    GPIO.cleanup()



