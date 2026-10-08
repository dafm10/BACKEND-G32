from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict
from uuid import UUID
from re import search

class RegistroUsuarioSchema(BaseModel):
    # EmailStr > valida que el texto tenga el formato nombre@dominio.com
    correo:EmailStr = Field(max_length=100)
    password:str = Field(max_length=128)
    nombre:str = Field(min_length=1)
    apellido:str | None = Field(default=None)

    @field_validator("correo")
    def normalizar_correo(cls, valor):
        return valor.lower()

    @field_validator("password")
    def validarPassword(cls, valor):
        errores = []

        if len(valor)<8:
            errores.append("El password no debe ser menor a 8 caracteres")

        # Expresiones Regulares (ReGex) es una forma de validar si un texto cumple o no con determinadas reglas sin importar su contenido, es decir: al menos una mayúscula, al menos una minúscula, al menos un número, al menos unn caracter especial
        if not search(r"[A-Z]", valor):
            errores.append("Falta una mayúscula")

        if not search(r"[a-z]", valor):
            errores.append("Falta una minúscula")

        # También se puede utilizar r"[0.9]"
        if not search(r"\d", valor):
            errores.append("Falta un número")

        if not search(r"[^A-Za-z0-9]", valor):
            errores.append("Falta un caracter especial")

        if errores:
            print(errores)
            raise ValueError(", ".join(errores))

        return valor


class LoginUsuarioSchema(BaseModel):
    correo: EmailStr
    password: str


class UsuarioSchema(BaseModel):
    # Poder recibir desde una instancia de la clase del modelo, sin la necesidad de pasarlo como diccionario
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    correo: EmailStr
    nombre: str
    apellido: str | None