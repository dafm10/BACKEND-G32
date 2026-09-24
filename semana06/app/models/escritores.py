from app.extensions import db
from sqlalchemy import Column, types
from enum import Enum

# Tenemos que crear un enumerador, es decir limitar a posibles valores
class EstadoEscritor(Enum):
    # Al heredad de la clase Enum, los atributos que coloquemos en esta clase se comportarán como valores para poder ser utilizados
    VIVO = 'VIVO'
    MUERTO = 'MUERTO'

class Escritor(db.Model):
    __tablename__ = 'escritores'
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellidos = Column(type_=types.Text, nullable=False)
    nacionalidad = Column(type_=types.Text)
    # Para colocar un valor por defecto, es decir, si al momento de crear un registro este no se le pasa el valor, entonces usará el valor definido en 'Default'
    estado = Column(type_=types.Enum(EstadoEscritor), nullable=False, default=EstadoEscritor.VIVO)