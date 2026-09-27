from pydantic import BaseModel, Field

# pydantic valida la configuración que nosotros definamos en los atributos de la clase, es decir utilizará la configuración de cada atributo para que cuando le pasemos la información esta sea corroborada y si es valida, continuará, si no, emitirá un error de validación
class CategoriaSerializer(BaseModel):
    nombre: str = Field(examples=["Cienca ficción", "Comedia"])