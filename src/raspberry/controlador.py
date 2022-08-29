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
<<<<<<< HEAD
        A="Ingreso al inidio del dia"
        print(A)
    dest=getRoutes(conn)
    
    print(dest)
    Ing=getDatosActuales(conn,dateCurrent)
    arduin=str(Ing[1])
    arduino(arduin)
    
    print(arduin)
    

=======
        #sendDatabySerial("A")
        print("Ingreso al inicio del dia")
    print(getRoutes(conn))
    print(getDatosActuales(conn,dateCurrent))
    conn.close ()
>>>>>>> 4770ed4d84fe0df9e32d4e7cd6b1d70bb5eff4e6

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
<<<<<<< HEAD
    
    des1=(getRoutes(conn))
    print(des1)
    Sal=(getDatosActuales(conn,dateCurrent))
    salard=str(Sal[1])
    arduino(salard)
    print(salard)

=======
    print(getRoutes(conn))
    print(getDatosActuales(conn,dateCurrent))
    conn.close()
>>>>>>> 4770ed4d84fe0df9e32d4e7cd6b1d70bb5eff4e6
