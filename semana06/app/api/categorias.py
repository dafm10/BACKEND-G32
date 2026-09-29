# Ahora todos los métodos (GET, POST, PUT, DELETE), se definirán como métodos de una clase
from flask_restful import Resource, request
from app.schemas import CategoriaSchema
from pydantic import ValidationError, TypeAdapter
from app.models import Categoria
from app.extensions import db

class CategoriasController(Resource):
    def get(self):
        # SELCT * FROM categorias;
        categorias = db.session.query(Categoria).all()
        print(categorias)
        # TypeAdapter es una clase que me permite modificar el Deserializador para poder agregarle que puedo pasarle un conjunto de instancias, ya que solamente aceptará una
        adaptador_categorias = TypeAdapter(list[CategoriaSchema])
        # validate_python > se usa para poder hacer la validación de la información proveniente de las instancias del modelo y convertirlas a instancias del Deserializador.
        resultado = adaptador_categorias.validate_python(categorias)
        print(resultado)
        return {
            "message": "Las categorías son:",
            # dump_python, convertimos el conjunto de instancias del Deserializador a un formato que pueda ser devuelto, es decir, en este caso uusaremos un formato json
            "content": adaptador_categorias.dump_python(resultado, mode="json")
        } # Su código de estado por defecto es 200

    def post(self):
        data = request.get_json()
        # Siempre hay que validar la data antes de mandarla a la BD
        # Si al momento de validar la información falla, emitirá un error de tipo ValidationError
        try:
            # Serializador es como un filtro que permite ver si la data que envia el cliente es correcta o no
            print(CategoriaSchema.model_json_schema())
            informacionSerializada = CategoriaSchema.model_validate(data)
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


class CategoriaController(Resource):
    # Esta clase será la encargada de la gestión de 1 sola categoría (según su ID)
    def validarCategoria(self, id):
         # filter > se usa en comparación > filter(Categoria.id == 1)
        # filter_by > se usa en asignación > filter_by(id=1)
        # SELECT * FROM categorias WHERE id = ... LIMIT 1;
        categoriaEncontrada = db.session.query(Categoria).filter(Categoria.id == id).first()
        return categoriaEncontrada

    def get(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message': 'Categoría no existe'
        }, 404
        
        respuesta = CategoriaSchema.model_validate(categoriaEncontrada).model_dump()

        return {
            'content': respuesta
        }

    def put(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message': 'Categoría no existe'
            }, 404

        categoriaValidada = CategoriaSchema.model_validate(request.get_json())

        # En la instancia que tengo de mi categoríaEncontrada puedo modificar la información
        categoriaEncontrada.nombre = categoriaValidada.nombre

        # para que los datos se guarden de manera permanente en la BD
        db.session.commit()

        # Ahora obtenemos la información actualizada desde la categoriaEncontrada para devolverala al cliente
        resultado =  CategoriaSchema.model_validate(categoriaEncontrada).model_dump()
        return {
            'message': 'Categoría modificada exitosamente',
            'content': resultado
        }

    def delete(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message': 'Categoría no existe'
            }, 404

        # DELETE FROM categorias WHERE id = ...;
        db.session.query(Categoria).filter(Categoria.id == id).delete()

        db.session.commit()

        # En los DELETE permanentes se suele no retornar nada y solo retornar un estado 204 (No Content)
        return None, 204