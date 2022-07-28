import os
from webbrowser import get   #de este modulo saco las variables de entorno para configurar la BBDD y configurar la API
from flask import Flask, g

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(    #variables de entorno
        SENDGRID_KEY = os.environ.get("SENDGRID_API_KEY"),        #servicio de correo gratuito
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        DATABASE_HOST = os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD = os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER = os.environ.get("FLASK_DATABASE_USER"),
        DATABASE = os.environ.get("FLASK_DATABASE")
    )

    return app 
