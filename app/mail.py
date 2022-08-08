from flask import (Blueprint, render_template)
from app.db import get_db

bp = Blueprint('mail',__name__, url_prefix="/") #nombre del blueprint, nombre de la aplicacion, ruta por defecto al iniciar la app

@bp.route('/', methods=['GET'])

def index():
    db,c = get_db()
    c.execute("SELECT * FROM email")
    mails = c.fetchall()

    
    return render_template('mails/index.html', mails=mails)