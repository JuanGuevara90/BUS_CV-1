import datetime 
from conexion import create_connection
import raspberry.utiles.getDateCurrent


fecha =getDateCurrent.getDate_Current()
conn = create_connection()

def buscarregistro(conn):
    #BUscar si hay un registro en la tabla Registro_Pasajeros
    sql_buscar = "select count(*) from Registro_Pasajeros"
    conn.execute(sql_buscar)

def ingresarregistro(conn):
    #Si no existen registro se inserta una fila
    sql_insert = "INSERT INTO Registro_Pasajeros (Fecha,Total_PasajerosActual,Total_Pasajeros) VALUES ('"+formatDate+"','1','1')"
    conn.execute(sql_insert)
    conn.commit()
    
def actualizarregistro(conn):
    #Si hay el registro actualizo y sumo uno en el campo Total_Pasajeros
    sql_update ="update  Registro_Pasajeros set Total_PasajerosActual=Total_PasajerosActual+1 where Fecha='"+formatDate+"'"
    conn.execute(sql_update)
    conn.commit()
    
def disponibilidadBus(formatDate,conn):
    sql_query= "select Total_PasajerosActual, aforo from Registro_Pasajeros WHERE Fecha:'"+formatDate+"'"
    cursor=conn.execute(sql_query)
    if (cursor.length()!=0):
        for i in cursor:
            Total_PasajerosActual=i[0]
            aforo=i[1]
            
            if (Total_PasajerosActual<aforo):
                return True
                return False
    return False

def existeRegistrosFechaActual(conn,fechaActual):
    sql_query= "select count(*) from Registro_Pasajeros WHERE Fecha:'"+fechaActual+"'"
    cursor=conn.execute(sql_query)
    if (cursor.length()!=0):
        return True
    return False
    

print(existeRegistrosFechaActual(conn , fecha))