from flask import Blueprint, render_template, session, current_app, request

views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST":
        print(request.form.get("id_articulo") + " cantidad: " + request.form.get("cantidad"))

    bd = current_app.bd
    cursor = bd.cursor()
    # Query datos artículos
    cursor.execute("SELECT ID, nombre_articulo, precio_kilo, peso_articulo, precio_articulo, marca_articulo FROM Articulo;")
    datos_artículos = cursor.fetchall()
    # Query datos categorías
    cursor.execute("SELECT DISTINCT categoria_padre FROM categoria;")
    datos_categorías = cursor.fetchall()
    return render_template("index.html", artículos=datos_artículos, categorías=datos_categorías)

@views.route("/protegido")
def protegido():
    if "username" in session:
        return "<p>Estas logreado! te dejo ver esto</p>"
    