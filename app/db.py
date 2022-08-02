import mysql.connector
import click 
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions


"""------------------DOCUMENTATION---------------
* current_app: can be used to access data about the running application,
including the configuration. This is useful for both developers using 
the framework and ones building extensions for Flask.

* g: is an object for storing data during the application context of a 
running Flask web app.

* with_appcontext is a Flask decorator in the flask.cli module that wraps 
a callback to guarantee it will be called with a script's application context. 
Any callbacks registered with app.cli are wrapped with this function by default.

* schema is a libray that allows to create data structures (tables, columns, relationships, ...)"""

def get_db():

    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config["DATABASE_HOST"],
            user = current_app.config["DATABASE_USER"],
            password = current_app.config["DATABASE_PASSWORD"],
            database = current_app.config["DATABASE"]
        )
        g.c = g.db.cursor(dictionary =True)
    
    return g.db, g.c

def close_db(e=None):
    
    db= g.pop('db',None)
    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    db.commit()

"""----------- BLOQUE PARA INICIALIZAR LA BASE DE DATOS DESDE LA TERMINAL --------------"""

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Base de datos inicializada")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)