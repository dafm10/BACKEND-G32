from os import getenv

# El archivo config servirá para setear (asignar) las variables que se usarán en flask, ya bien sea en development o producción

class Base:
    # esta propiedad sirve para poder indicar si queremos que SQLALCHEMY nos muestre el seguimiento de las modificaciones en la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Base):
    DEBUG = True # Esta propiedad permitirá que se actualice automáticamente el servidor al guardar cualquier cambio
    # Esta variable sirve para obtener la cadena de conexión a nuestra BD
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")

class Production(Base):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")

# Diccionario con el mapeo de todas las opciones de configuración, se puede tener más en el caso que tengamos Stagin, PreProduction, Debuggin, etc.
config_map = {
    "development": Development,
    "production": Production
}