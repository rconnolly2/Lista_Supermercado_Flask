import mysql.connector
import os

ruta_este_archivo = os.path.dirname(os.path.abspath(__file__)) # la ruta absoluta que contiene este archivo .py
host="localhost"
user="root"
password="Hola"
database="lista_compra"

def crear_bd():
    nombre_bd = "lista_compra"
    # conexión:
    conexion_bd = mysql.connector.connect(host=host, user=user, password=password)
    cursor = conexion_bd.cursor()
    try:
        cursor.execute("CREATE DATABASE " + nombre_bd + ";")
        print("Bases de datos lista_compra creada correctamente!")
    except mysql.connector.Error as error:
        print("Error al crear base de datos: " + str(error))
    finally:
        cursor.close()
        conexion_bd.close() # cierro conexión

def crear_tablas():
    conexion_bd = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conexion_bd.cursor()
    archivo_sql = open((ruta_este_archivo + "\models\crear_tablas.sql"), "r")
    sql = archivo_sql.read()
    archivo_sql.close()

    # Añado tablas:
    try:
        cursor.execute(sql) # código sql
    except mysql.connector.Error as error:
        print("Error al crear tablas: " + str(error))
    finally:
        cursor.close()
        conexion_bd.close() # cierro conexión
        
def registrar_usuario(email, password):
    '''
    Para evitar Inyecciones 
    '''