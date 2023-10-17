from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return "<h1>Esto es la pagina de login!</h1>"

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/registrar")
def registrar():
    return render_template("register.html")