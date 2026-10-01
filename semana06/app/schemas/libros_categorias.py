from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator
from typing import Annotated

# Annotated > agrega información adicional a un tipo de datos, pertenece al módulo nativo de python
# En el Annotated, estamos indicando que ListaIds será de tipo list[PositivInt] y además estaremos agregando el argumento para pydantic que este será también un tipo Field con una longitud minima de 1 y máxima de 100
ListaIds = Annotated[list[PositiveInt], Field(min_length=1, max_length=100)]

class LibrosCategoriasSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    libroId: int = Field(min=1)
    categoriaIds: ListaIds = Field()

    # Si queremos agregar alguna validación a alguna de las propiedades del Schema, podemos hacerlo mediante el decorador, y en su parámetro indicar que propiedad(es) vamos a agregar esa validación
    @field_validator('categoriaIds')
    def eliminar_duplicados(cls, valor):
        # cls > es la misma instancia de la clase del atributo que en este caos sería Field
        # valor > es el valor que será validado
        # al convertirlo en un diccionario temporal lo que hace es que si la llave ya existe la sobreescribe y por ende al momento de retornar las llaves no habrá ninguna llave repetida y luego eso lo convertimos a una lista
        # fromkeys > crea un diccionario desde un iterable
        # el método fromkeys de un diccionario, crea un nuevo diccionario usando los valores de la lista como llaves y sus valores son None
        # al usar un diccionario para convertirlo a lista, agarra esas llaves y las colocará en la nueva lista, y sus valores los desechará
        # IDEAR OTRA FORMA EN LA CUAL PODAMOS RETIRAR LOS VALORES DUPLICADOS DE UNA LISTA
        # resultado = []
        # for elemento in valor:
        #     if elemento not in resultado:
        #         resultado.append(elemento)
        # return resultado
    
        # return list(dict.fromkeys(valor))
        return list(set(valor))