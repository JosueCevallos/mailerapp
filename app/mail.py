from crypt import methods
from flask import (Blueprint)

bp = Blueprint('mail',__name__, url_prefix="/") #nombre del blueprint, nombre de la aplicacion, ruta por defecto al iniciar la app

@bp.route('/', methods=['GET'])

def index():
    return 'prueba'