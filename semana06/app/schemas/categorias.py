from pydantic import BaseModel, Field, ConfigDict

# pydantic valida la configuración que nosotros definamos en los atributos de la clase, es decir utilizará la configuración de cada atributo para que cuando le pasemos la información esta sea corroborada y si es valida, continuará, si no, emitirá un error de validación
class CategoriaSerializer(BaseModel):
    # Serializador: es el encargado de validar la data que llega de afuera y verificar si es correcta
    nombre: str = Field(examples=["Cienca ficción", "Comedia"])

class CategoriaDeserializer(BaseModel):
    # Deserializador: Transforma la data proveniente de mi entorno (python) y devolverá en un formato legible (dict | json)
    # model_config es un atributo propio de la clase BaseModel que sirve para modificar todo el modelo en su totalidad, y no solamente un solo atributo
    # ConfigDict > sirve para indicar que la información que vamos a pasarle a este deserializador se realizara en formato de instancias y no en formato de un dict
    model_config = ConfigDict(from_attributes=True)

    # A los deserializadores no es nevesario agregarles restricciones ya que solo se usará para convertir la data de instancias de clases a dict
    id: int
    nombre: str



# Esta forma sería la opción corta usando Serializer y Deserializer 
class CategoriaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    # Para cuando se intente crear una nueva categoría, el ID no debe de enviarse
    # Al poner None, indicaremos que esta propiedad puede ser opcional
    id: int | None = Field(default=None)
    nombre: str = Field(min_length=1, examples=["Ciencia Ficción", "Comedia"])