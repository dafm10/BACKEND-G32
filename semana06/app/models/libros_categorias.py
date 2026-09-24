from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class LibroCategoria(db.Model):
    __tablename__ = 'libros_categorias'
    libroId = Column(
        ForeignKey(column='libros.id'), 
        nullable=False, 
        name='libro_id', 
        primary_key=True, 
        type_=types.Integer)
    
    categoriaId = Column(
        ForeignKey(column='categorias.id'), 
        nullable=False, 
        name='categoria_id', 
        primary_key=True, 
        type_=types.Integer)

    # Relationships
    # es la relación pero a nivel del ORM, es decir, esto no afecta en la BD pero me sirve para poder acceder a los datos desde una entidad (libros) hacia sus libros categoria
    # El relationship, creará un atributo en tiempo de ejecución para poder acceder desde la instancia del libro hacia todos sus libro_categorias
    libros = relationship('Libro', backref='libro_categoria')
    categorias = relationship('Categoria', backref='libro_categoria')