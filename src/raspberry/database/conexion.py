import sqlite3
from sqlite3 import Error
# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PATH_DATABASE = os.environ.get("DATABASE")

database = PATH_DATABASE

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
        

    
def main():
    
    try:
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Registro_Pasajeros (
                                            Fecha TIMESTAMP PRIMARY KEY,
                                            Total_PasajerosDia integer,
                                            Total_Pasajeros integer NOT NULL,
                                            Aforo interger
                                        ); """

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Bus (
                                        origen text,
                                        destino text
                                    );"""

        # create a database connection
        conn = create_connection(database)

        # create tables
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)

            # create tasks table
            create_table(conn, sql_create_tasks_table)
            print("Ingreso correcto")
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)
        

main()