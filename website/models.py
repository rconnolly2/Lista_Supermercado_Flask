import mysql.connector
import os
import hashlib

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
        
def registrar_usuario(email: str, password_usuario: str, conexion_bd):
    '''
    Para evitar Inyecciones SQL utilizamos queries parametrizada

    email => El email del usuario nuevo

    password => Password del usuario sin encriptar
    '''
    try:
        usuario, _ = email.split("@") # cojo el usuario del correo
        obj_hash = hashlib.sha256()
        obj_hash.update(password_usuario.encode("utf-8")) # encripto con sha256
        password_usuario_hex = str(obj_hash.hexdigest()) # resultado encriptado contraseña hexadecimal
        cursor = conexion_bd.cursor()

        # Creo usuario en nuestra tabla usuarios:
        parameterized_insert_query = """ INSERT INTO Usuario(nombre_usuario, correo_usuario, password_usuario)
                                    VALUES(%s, %s, %s);"""
        #Ejecuto el insert query:
        cursor.execute(parameterized_insert_query, (usuario, email, password_usuario_hex))
        conexion_bd.commit()
        print("Datos insertados correctamente!")
    except mysql.connector.Error as error:
        print("Hubo un error al ejecutar INSERT:" + str(error))
    finally:
        cursor.close() # cierro cursor conexión sql sigue abierta

