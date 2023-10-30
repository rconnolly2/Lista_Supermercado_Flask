from flask import Blueprint, render_template, session, current_app

views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
def index():
    bd = current_app.bd
    cursor = bd.cursor()
    cursor.execute("SELECT ID, nombre_articulo, precio_kilo, peso_articulo, precio_articulo, marca_articulo FROM Articulo;")
    datos_artículos = cursor.fetchall()
    
    return render_template("index.html", artículos=datos_artículos)

@views.route("/protegido")
def protegido():
    if "username" in session:
        return "<p>Estas logreado! te dejo ver esto</p>"
    