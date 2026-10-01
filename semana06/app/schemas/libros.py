from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class LibroSchema(BaseModel):
    # Si vamos a querer convertir la información de instancias (del modelo) a diccionario, entonces tenemos que modificar la configuración de todo el schema, indicandole que hora también podremos recibir la información proveniente de las instancias.
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field(default=None)
    nombre: str = Field(min_length=1, examples=["Python Fundamentals", "Python for dummys"])
    fechaPublicacion: date | None = Field(default=None, examples=["2026-09-28"])
    prologo: str | None
    isbn: str = Field(max_length=20)
    # Esta propiedad no debe ser utilizada por el cliente, jamás la debe observar
    # exclude=True > evita que aparezca al listar
    # eliminado: bool = Field(default=False, exclude=True)