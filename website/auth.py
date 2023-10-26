from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for, session
import hashlib
from website.models import registrar_usuario
auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return "<h1>Esto es la pagina de login!</h1>"

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        bd = current_app.bd
        cursor = bd.cursor()
        cursor.execute("SELECT correo_usuario, password_usuario FROM Usuario")
        correos_passwords_bd = cursor.fetchall()
        cursor.close() # cierro cursor conexión sql sigue abierta
        print(correos_passwords_bd)
        email = request.form.get("email")
        password = request.form.get("password")
        username = email.split("@")[0]
        # hash sha256 de contraseña usuario:
        obj_hash = hashlib.sha256()
        obj_hash.update(password.encode("utf-8")) # encripto a sha256 para integridad
        hash_hex_password = str(obj_hash.hexdigest()) # valor hexadecimal

        if "temp-mail.org" in email.split("@"):
            flash("¡No aceptamos este tipo de email!", category="error")
        else:
            for datos in correos_passwords_bd:
                print(hash_hex_password, datos[1])
                if email == datos[0] and hash_hex_password == datos[1]: # Misma contraseña y password:
                    flash("Login valido!", category="info")
                    session["username"] = username
                    print(session)



    return render_template("login.html")

@auth.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        bd = current_app.bd
        cursor = bd.cursor()
        cursor.execute("SELECT correo_usuario, password_usuario FROM usuario;")
        correos_passwords_bd = cursor.fetchall()
        email, password = request.form.get("email"), request.form.get("password")

        if "temp-mail.org" in email.split("@") or "@" not in email:
            flash("¡No aceptamos este tipo de email!", category="error")
        elif len(password) <= 6:
            flash("¡Contraseña muy corta! tiene que tener mas de 6 caracteres", category="error")
        elif any(n in password for n in ["1", "2", "3", "4" ,"5" ,"6" ,"7" , "8", "9"]) == True: # Miro si tiene números la password
            # Creo usuario en BD:
            registrar_usuario(email, password, bd)
            flash("¡Usuario registrado!", category="info")
            return redirect(url_for("auth.login"))
        else:
            flash("¡La contraseña tiene que contener números!", category="error")
    
        

    return render_template("register.html")