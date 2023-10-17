import mysql.connector

def crear_bd():
    nombre_bd = "lista_compra"
    # conexión:
    conexion_bd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hola"
    )
    cursor = conexion_bd.cursor()
    try:
        cursor.execute("CREATE DATABASE " + nombre_bd + ";")
        print("Bases de datos lista_compra creada correctamente!")
    except mysql.connector.Error as error:
        print("Error al crear base de datos: " + error)
    finally:
        cursor.close()
        conexion_bd.close() # cierro conexión
