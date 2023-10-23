from flask import Flask
import mysql.connector
from .views import views
from .auth import auth
from .models import crear_bd, crear_tablas

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Mi contraseña"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "Hola"
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_DB"] = "lista_compra"

    
    try:
        bd = mysql.connector.connect(
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DB']
        )
    except mysql.connector.errors.ProgrammingError: # Si me da error al hacer conexión con la BD:
        crear_bd() # creo la base de datos si no existe
        crear_tablas() # creo tablas

    
    #Añado mi conexión de la base de datos al contexto de aplicación:
    app.bd = bd
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")
    return app