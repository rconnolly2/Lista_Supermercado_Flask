from flask import Blueprint, render_template, request, current_app

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return "<h1>Esto es la pagina de login!</h1>"

@auth.route("/login", methods=["GET", "POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    print(email, password)
    return render_template("login.html")

@auth.route("/registrar")
def registrar():
    bd = current_app.bd
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM usuario;")
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template("register.html")