from flask import Blueprint, render_template, session, current_app, request
from .models import dame_categorías

views = Blueprint("views", __name__)
lista_categorías = dame_categorías()
dic_cat = dame_categorías(True)


@views.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST" and "username" in session:
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


@views.route("/<categoria>", methods=["POST", "GET"])
def categoria(categoria):
    if categoria in [cat[0] for cat in lista_categorías]: # comprensión de lista
        bd = current_app.bd
        cursor = bd.cursor()
        # Query datos artículos de la categoria seleccionada
        cursor.execute("SELECT * FROM Articulo WHERE ID_categoria in (SELECT ID_categoria FROM categoria WHERE categoria_padre='" + categoria + "');")
        datos_artículos = cursor.fetchall()
        return render_template("categorias.html", categorías=lista_categorías, categoría_sel=categoria, dict_categorías=dic_cat, artículos=datos_artículos)
    else:
        return "<h1>Nada</h1>"


def subcategoria_valida(categoria_sel: str) -> bool:
    l_subcat = [dic_cat[cat] for cat in dic_cat]
    for i in range(len(l_subcat)):
        for j in range(len(l_subcat[i])):
            if categoria_sel==l_subcat[i][j]:
                return True
            
    return False # si no encuentra devuelvo false


@views.route("/subcategoria/<categoria>", methods=["POST", "GET"])
def subcategoria(categoria):
    if subcategoria_valida(categoria):
        bd = current_app.bd
        cursor = bd.cursor()
        # Query datos artículos de la categoria seleccionada
        cursor.execute("SELECT * FROM Articulo WHERE ID_categoria in (SELECT ID_categoria FROM categoria WHERE nombre_categoria='" + categoria + "');")
        datos_artículos = cursor.fetchall()
        return render_template("categorias.html", categorías=lista_categorías, categoría_sel=categoria, dict_categorías=dic_cat, artículos=datos_artículos)
    else:
        return "<h1>Nada</h1>"
        

@views.route("/protegido")
def protegido():
    if "username" in session:
        return "<p>Estas logreado! te dejo ver esto</p>"
    