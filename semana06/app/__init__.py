from flask import Flask
from .config import config_map
from .models import *
from .extensions import db, migrate

# Al usar el patron de diseño Application Factory se recomienda crear una función llamada: create_app, en la cual se inicializará todo el proyecto y así mismo puede recibir parámetros para los diferentes entornos de prueba
def create_app(env = "development"):
    app = Flask(__name__)
    # from_object > actualiza los valores que le pasemos en el parámetro para que la instancia de Flask arranque con esas modificiones de sus parámetros. Por ejemplo: Debug, entre otros
    app.config.from_object(config_map[env])

    # Inicializamos la instancia de la BD pasándole la instancia de Flask para que utilice las variables que hemos configurado en la instancia (config_map)
    db.init_app(app)

    # Inicializamos la instancia de las migraciones para ahora declarar nuestra configuración de la instancia de Flask y nuestra configuración de la BD
    migrate.init_app(app, db)

    return app