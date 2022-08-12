from .utiles.getDateCurrent import getDate_Current
from .database.operaciones import existeRegistrosFechaActual,ingresarRegistro,disponibilidadBus,actualizarRegistroSuma,actualizarRegistroResta,validateLeft
from .database.conexion import create_connection

def controladorIngreso():
    conn = create_connection()
    dateCurrent = getDate_Current()
    if(existeRegistrosFechaActual(conn,dateCurrent)):
        if(disponibilidadBus(conn,dateCurrent)):
            actualizarRegistroSuma(conn,dateCurrent)
            """ Actualizar y enviar al arduino"""
            print("Ingreso un pasajero")
        else:
            """ Enviar al arduino bloqueado la puerta """
            print("Pruerta Bloqueada")
    else:
        """ Enviar al arduino """
        ingresarRegistro(conn,dateCurrent)
        print("Ingreso al inicio del dia")

def controladorSalida():
    conn = create_connection()
    dateCurrent = getDate_Current()
    if(existeRegistrosFechaActual(conn,dateCurrent)):
        if(validateLeft(conn,dateCurrent)):
            actualizarRegistroResta(conn,dateCurrent)
            """ Actualizar y enviar al arduino"""
            print("Ingreso un pasajero")
        else:
            print("Enviar al arduino ")
    else:
        ingresarRegistro(conn,dateCurrent)
        print("Ingreso al inicio del dia")
    
""" controladorIngreso() """
""" controladorSalida() """