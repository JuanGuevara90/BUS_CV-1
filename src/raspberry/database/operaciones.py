from sqlite3 import Error
from .conexion import create_connection
from ..utiles.getDateCurrent import getDate_Current


def ingresarRegistroPasajeros(conn,fechaActual):
    try:
        sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_Pasajeros,Total_PasajerosDia,Aforo) VALUES ('"+fechaActual+"','1','1','5')"
        conn.execute(sql_insert)
        conn.commit()
    except Error as e:
        print(e)
    
def actualizarRegistroSuma(conn,fechaActual):
    try:
        sql_update ="update  Registro_Pasajeros set Total_PasajerosDia=Total_PasajerosDia+1 ,Total_Pasajeros=Total_Pasajeros+1 where Fecha='"+fechaActual+"'"
        conn.execute(sql_update)
        conn.commit()
    except Error as e:
        print(e)

def actualizarRegistroResta(conn,fechaActual):
    try:
        sql_update ="update  Registro_Pasajeros set Total_Pasajeros=Total_Pasajeros-1 where Fecha='"+fechaActual+"'"
        conn.execute(sql_update)
        conn.commit()
    except Error as e:
        print(e)
    
def disponibilidadBus(conn,fechaActual):
    try:
        sql_query= "select Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            Total_PasajerosActual=i[0]
            aforo=i[1]
            if (Total_PasajerosActual<aforo):
                return True
            return False
    except Error as e:
        print(e)
    
    
def validateLeft(conn,fechaActual):
    try:
        sql_query= "select Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            Total_PasajerosActual=i[0]
            if (Total_PasajerosActual>0):
                return True
            return False
    except Error as e:
        print(e)

def existeRegistrosFechaActual(conn,fechaActual):
    try:
        sql_query= "select count(*) from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
        cursor=conn.execute(sql_query)
        for i in cursor:
            if (i[0]>0):
                return True
            return False
    except Error as e:
        print(e)
    