from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum

class EstadoEjemplar(Enum):
    DISPONIBLE = 'DISPONIBLE'
    PRESTADO = 'PRESTADO'
    NO_DISPONIBLE = 'NO_DISPONIBLE'

class Ejemplar(db.Model):
    __tablename__ = 'ejemplares'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    codigoInventario = Column(type_=types.VARCHAR(100), nullable=False, name='codigo_inventario')
    estado = Column(type_=types.Enum(EstadoEjemplar), default=EstadoEjemplar.DISPONIBLE)
    libroId = Column(ForeignKey('libros.id'), type_=types.Integer, nullable=False, name='libro_id')
    # No incluye en la creación y mantenimiento de la tabla
    # relationship crea un atributo en las clases Ejmplear y Libro que servirán para poder acceder a su información anidada, es decir, desde el ejemplar podemos acceder a que Libro pertenece y desde el Libro podemos acceder a todos sus ejemplares mediante, en este caso, el nombre definido en el back_ref. Entonces si ponemos 
    # libro1 = Libro () obtenemos el registro de la bd
    # libro1.ejemplares > dara toda la lista de los ejemplares que pertenecen a ese libro en formato de Lista
    # [<Ejemplar1>, <Ejemplar2>, ...]
    # ejemplarcito = obtengo mi registro de ejemplar de la bd
    # ejemplarcito.libro > devolverá el libro al cual pertenece el ejemplar
    libro = relationship('Libro', backref='ejemplares')