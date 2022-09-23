from .utiles.getDateCurrent import getDate_Current
import RPi.GPIO as GPIO
from .database.operaciones import Asientosdisponibles, existeRegistrosFechaActual,ingresarRegistroPasajeros,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft,getDatosActuales,getRoutes
from .database.conexion import create_connection,main,isSqlite3Db
from .serial.sendData import sendDatabySerial,arduino
from .serial.sensorica import sensorica
import os
from dotenv import load_dotenv
from os.path import join, dirname
from .vista.MostrarDatos import agregar


def controladorIngreso():
    if(controladorSensorIngreso):
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
            A="Ingreso al inidio del dia"
            print(A)

        Ing=SendData(conn,dateCurrent)
        agregar(Ing)
        enarduin=str(Ing[1])
        sendDatabySerial(enarduin)
        print(enarduin)

def controladorSalida():
    if(controladorSensorSalida()):
        if( isSqlite3Db() ): 
            conn = create_connection()
            dateCurrent = getDate_Current()
            if( existeRegistrosFechaActual( conn , dateCurrent )):
                if( validateLeft( conn , dateCurrent )):
                    actualizarRegistroResta( conn , dateCurrent )
                    """ Actualizar y enviar al arduino"""
                    B="Ingreso un pasajersso"
                
                    print(B)               
                else:
                    print("Enviar al arduino ")   
            Sal=SendData(conn,dateCurrent)
            salard=str(Sal[1])
            sendDatabySerial(salard)
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
    TRIG = os.environ.get("TRIG")
    ECHO = os.environ.get("ECHO")
    distanciaS1=int(sensorica(TRIG,ECHO))
    if(distanciaS1<100 ):
         n=True
         return n
    GPIO.cleanup()

def controladorSensorSalida():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    TRIG1 = os.environ.get("TRIG1")
    ECHO1 = os.environ.get("ECHO1")
  
    distanciaS2=int(sensorica(TRIG1,ECHO1))
    if(distanciaS2<100 ):
         n=True
         return n
    GPIO.cleanup()