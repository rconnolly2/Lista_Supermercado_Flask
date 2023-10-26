from flask import Blueprint, render_template, session

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/protegido")
def protegido():
    if "username" in session:
        return "<p>Estas logreado! te dejo ver esto</p>"
    