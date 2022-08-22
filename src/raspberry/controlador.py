from .utiles.getDateCurrent import getDate_Current
from .database.operaciones import existeRegistrosFechaActual,ingresarRegistroPasajeros,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft,getDatosActuales,getRoutes
from .database.conexion import create_connection,main,isSqlite3Db
from .serial.sendData import sendDatabySerial

def controladorIngreso():
    if( isSqlite3Db() ): 
        conn = create_connection()
    else:
        conn = main()
    dateCurrent = getDate_Current()
    if( existeRegistrosFechaActual( conn , dateCurrent)  ):
        if( disponibilidadBus( conn , dateCurrent ) ):
            actualizarRegistroSuma( conn , dateCurrent )
            """ Actualizar y enviar al arduino"""
            #sendDatabySerial("A")
            print("Ingreso un pasajero")
        else:
            """ Enviar al arduino bloqueado la puerta """
            #sendDatabySerial("B")
            print("Puerta Bloqueada")
    else:
        """ Enviar al arduino """
        ingresarRegistroPasajeros( conn , dateCurrent )
        #sendDatabySerial("A")
        print("Ingreso al inicio del dia")
    print(getRoutes(conn))
    print(getDatosActuales(conn,dateCurrent))

def controladorSalida():
    if( isSqlite3Db() ): 
        conn = create_connection()
        dateCurrent = getDate_Current()
        if( existeRegistrosFechaActual( conn , dateCurrent )):
            if( validateLeft( conn , dateCurrent )):
                actualizarRegistroResta( conn , dateCurrent )
                """ Actualizar y enviar al arduino"""
                #sendDatabySerial("A")
                print("Ingreso un pasajero")
            else:
                print("Enviar al arduino ")
    print(getRoutes(conn))
    print(getDatosActuales(conn,dateCurrent))