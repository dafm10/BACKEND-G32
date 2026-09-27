from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    fechaPrestamos = Column(type_=types.Date, nullable=False, name='fecha_prestamos')
    fechaDevolucion = Column(type_=types.Date, nullable=False, name='fecha_devolucion')
    usuarioId = Column(ForeignKey('usuarios.id'), type_=types.Integer, nullable=False, name='usuario_id')
    ejemplarId = Column(ForeignKey('ejemplares.id'), type_=types.Integer, nullable=False, name='ejemplar_id')

    usuario = relationship('Usuario', backref='prestamos')
    ejemplar = relationship('Ejemplar', backref='prestamos')