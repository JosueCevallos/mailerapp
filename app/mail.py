from distutils.log import error
import email
from flask import (Blueprint, flash, render_template, request)
from app.db import get_db

bp = Blueprint('mail',__name__, url_prefix="/") #nombre del blueprint, nombre de la aplicacion, ruta por defecto al iniciar la app

@bp.route('/', methods=['GET'])

def index():
    db,c = get_db()
    c.execute("SELECT * FROM email")
    mails = c.fetchall()

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET','POST'])
def create():

    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        content = request.form.get("content")
        errors = []

        if not email:
            errors.append("El email es obligatorio")
        if not subject:
            errors.append("El asunto es obligatorio")
        if not content:
            errors.append("El contenido es obligatorio")

        if len(errors) == 0:
            pass
        else:
            for error in errors:
                flash(error)

    return render_template('mails/create.html')