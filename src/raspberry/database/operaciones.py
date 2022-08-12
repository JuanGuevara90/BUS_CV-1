from .conexion import create_connection
from ..utiles.getDateCurrent import getDate_Current

def buscarregistro(conn):
    #BUscar si hay un registro en la tabla Registro_Pasajeros
    sql_buscar = "select count(*) from Registro_Pasajeros"
    conn.execute(sql_buscar)

def ingresarRegistro(conn,formatDate):
    sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_Pasajeros,Total_PasajerosDia,Aforo) VALUES ('"+formatDate+"','1','1','5')"
    conn.execute(sql_insert)
    conn.commit()
    
def actualizarRegistroSuma(conn,formatDate):
    #Si hay el registro actualizo y sumo uno en el campo Total_Pasajeros
    sql_update ="update  Registro_Pasajeros set Total_PasajerosDia=Total_PasajerosDia+1 ,Total_Pasajeros=Total_Pasajeros+1 where Fecha='"+formatDate+"'"
    conn.execute(sql_update)
    conn.commit()

def actualizarRegistroResta(conn,formatDate):
    #Si hay el registro actualizo y sumo uno en el campo Total_Pasajeros
    sql_update ="update  Registro_Pasajeros set Total_Pasajeros=Total_Pasajeros-1 where Fecha='"+formatDate+"'"
    conn.execute(sql_update)
    conn.commit()
    
def disponibilidadBus(conn,formatDate):
    sql_query= "select Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+formatDate+"'"
    cursor=conn.execute(sql_query)
    for i in cursor:
        Total_PasajerosActual=i[0]
        aforo=i[1]
        if (Total_PasajerosActual<aforo):
            return True
        return False
    
def validateLeft(conn,formatDate):
    sql_query= "select Total_Pasajeros, Aforo from Registro_Pasajeros WHERE Fecha='"+formatDate+"'"
    cursor=conn.execute(sql_query)
    for i in cursor:
        Total_PasajerosActual=i[0]
        if (Total_PasajerosActual>0):
            return True
        return False

def existeRegistrosFechaActual(conn,fechaActual):
    sql_query= "select count(*) from Registro_Pasajeros WHERE Fecha='"+fechaActual+"'"
    cursor=conn.execute(sql_query)
    for i in cursor:
        if (i[0]>0):
            return True
        return False
    
""" print(existeRegistrosFechaActual(conn , fecha)) """