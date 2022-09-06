from .utiles.getDateCurrent import getDate_Current
from .database.operaciones import Asientosdisponibles, existeRegistrosFechaActual,ingresarRegistroPasajeros,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft,getDatosActuales,getRoutes
from .database.conexion import create_connection,main,isSqlite3Db
from .serial.sendData import sendDatabySerial,arduino

def controladorIngreso():
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
    dest=getRoutes(conn)
    
    print(dest)
    Ing=getDatosActuales(conn,dateCurrent)
    arduin=str(Ing[1])
    arduino(arduin)
    
    print(arduin)

def controladorSalida():
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
    des1=(getRoutes(conn))
    print(des1)
    Sal=(getDatosActuales(conn,dateCurrent))
    salard=str(Sal[1])
    arduino(salard)
    print(salard)

def controladorEnvioDatos():
    if( isSqlite3Db() ): 
        conn = create_connection()
        dateCurrent = getDate_Current()
    getdata=(getDatosActuales(conn,dateCurrent))
    return getdata
    