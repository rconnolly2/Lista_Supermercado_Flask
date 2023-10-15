from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return "<h1>Esto es la pagina de login!</h1>"