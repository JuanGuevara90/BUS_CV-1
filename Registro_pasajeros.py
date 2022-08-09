import sqlite3
import datetime 
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def ingresarPasajero(conn):
    #BUscar si hay un registro en la tabla Registro_Pasajeros
    sql_buscar = "select count(*) from Registro_Pasajeros"
    conn.execute(sql_buscar)
    
    #Si no existen registro se inserta una fila
    currentDatetime = datetime.datetime.now()
    print(currentDatetime.strftime("%y-%m-%d %H:%M:%S"))
    formatDate = currentDatetime.strftime("%y-%m-%d %H:%M:%S")
    #conn.execute("INSERT INTO Registro_Pasajeros (Total_Pasajeros, fecha) VALUES (%s,%s)",(1,formatDate))
    sql_insert = "INSERT INTO Registro_Pasajeros (Total_Pasajeros, fecha) VALUES ('1','"+formatDate+"')"
    conn.execute(sql_insert)
    
    #Si hay el registro actualizo y sumo uno en el campo Total_Pasajeros
    #nuevo_valor = Total_Pasajeros+1
    sql_update ="update  Registro_Pasajeros set Total_Pasajeros=Total_pasajeros+1 where id=1"
    conn.execute(sql_update)
    
    #Si hay 


def main():
    
    database = r"C:\Users\Jessica\Desktop\Face\DB SQLite\faceDatabase.db"
 

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Registro_Pasajeros (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Total_Pasajeros integer,
                                        Fecha TIMESTAMP NOT NULL
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Bus (
                                    origen text,
                                    destino text,
                                    aforo interger
                                
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        ingresarPasajero(conn)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
        print("Ingreso correcto")
    else:
        print("Error! cannot create the database connection.")

main()