from flask import Blueprint, render_template, request, current_app, flash, redirect

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return "<h1>Esto es la pagina de login!</h1>"

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        bd = current_app.bd
        cursor = bd.cursor()
        cursor.execute("SELECT correo_usuario, password_usuario FROM Usuario;")
        correos_passwords_bd = cursor.fetchall()
        email = request.form.get("email")
        password = request.form.get("password")

        if "temp-mail.org" in email.split("@"):
            flash("¡No aceptamos este tipo de email!", category="error")
        else:
            for datos in correos_passwords_bd:
                if email == datos[0] and password == datos[1]: # Misma contraseña y password:
                    flash("Login valido!", category="info")
                else:
                    flash("Login invalido, revisa tu usuario y contraseña", category="error")

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