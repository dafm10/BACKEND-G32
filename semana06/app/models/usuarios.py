from app.extensions import db
from sqlalchemy import Column, types

# Las tablas de las bases de datos van a ser clases en Python
# Al heredar la clase Mode estamos indicando a SQLAlchemy que esta clase va a ser mapeada como una tabla en la BD
class Usuario(db.Model):
    # La clase Model usa el atributo __tablename__ para indicar como se llamará esta table en la BD
    __tablename__ = 'usuarios'

    # Ahora mapeamos todas las columnas como si fueran atributos de la clase, en este caso no se usa constructores ya que la clase Model lo maneja de manera diferente
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#module-sqlalchemy.types
    # O bien podemos usar sqlalchemy.Column o de la misma instancia de db podemos usar la clase Column
    id  = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)
    # name sirve para indicar como se llamará la columna en la bd
    apellidoPaterno = Column(name='apellido_pat', type_=types.Text, nullable=False)
    apellidoMaterno = Column(name='apellido_mat', type_=types.Text)
    # Si no pondemos name en el constructor de la clase Column, el name será el nombre del atributo, solo se debe colocar name cuando el nombre del atributo será diferente del nombre de la tabla en la BD
    # name es como se llamará la columna en la BD
    correo = Column(type_=types.Text, unique=True, nullable=False)
    fechaNacimiento = Column(name='fecha_nacimiento', type_=types.Date)