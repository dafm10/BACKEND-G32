# Ahora todos los métodos (GET, POST, PUT, DELETE), se definirán como métodos de una clase
from flask_restful import Resource, request
from app.schemas import CategoriaSerializer
from pydantic import ValidationError
from app.models import Categoria
from app.extensions import db

class CategoriaController(Resource):
    def get(self):
        return {
            "message": "Las categorías son:"
        } # Su código de estado por defecto es 200

    def post(self):
        data = request.get_json()
        # Siempre hay que validar la data antes de mandarla a la BD
        # Si al momento de validar la información falla, emitirá un error de tipo ValidationError
        try:
            informacionSerializada = CategoriaSerializer.model_validate(data)
            print(informacionSerializada)

            # Ahora que sabemos que la información es correcta, procedemos con el guardado en la base de datos
            # INSERT INTO categorias (nombre) VALUES (...);
            nuevaCategoria = Categoria(nombre = informacionSerializada.nombre)
            # Acá agregamos el nuevo registro a la BD
            db.session.add(nuevaCategoria)
            # Guardamos el registro de manera permanente
            db.session.commit()

            return {
                "message": "Categoría creada exitosamente"
            }, 201 # Created
        except ValidationError as error:
            return {
                "message": "Error al crear la categoría",
                "content": error.errors()
            }, 405 # Bad Request