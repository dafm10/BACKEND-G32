from app.extensions import db
from sqlalchemy import Column, types

class Libros(db.Model):
    __tablename__ = 'libros'
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    fechaPublicacion = Column(name='fecha_publicacion', type_=types.Date)
    prologo = Column(type_=types.Text)
    isbn = Column(type_=types.VARCHAR(20), unique=True, nullable=False)