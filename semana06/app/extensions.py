from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Acá inicializamos el uso del ORM
db = SQLAlchemy()

# Aca inicializamos el uso del administrador de migraciones de la BD
# encargado de hacer toda la administración, registro y mantenimiento de la BD
migrate = Migrate()