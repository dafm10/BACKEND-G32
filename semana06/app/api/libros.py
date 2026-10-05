from flask_restful import Resource, request
from app.schemas import LibroSchema
from pydantic import ValidationError, TypeAdapter
from datetime import datetime
from app.models import Libro
from app.extensions import db
from app.schemas import LibroSchema

class LibrosController(Resource):
    def get(self):
        libros = db.session.query(Libro).filter(Libro.eliminado == False).all() # obtenemos todos los libros

        adapter_libros = TypeAdapter(list[LibroSchema])
        resultado = adapter_libros.validate_python(libros)
        
        return {
            "message": "Los libros son:",
            "content": adapter_libros.dump_python(resultado, mode="json") # dump_python > convierte a una lista de diccionarios
        }

    def post(self):
        data = request.get_json()
        try:
            libroSerializado = LibroSchema.model_validate(data)
            # Cuando una instancia de clase, una función, un método espera recibir un conjunto de parámetros definidos por nombres
            # Libro(nombre='...', isbn='...', eliminado='...', prologo='...', fechaPublicacion='...')
            # Pero si tenemos la información en un dict
            # {
            # "nombre":"...",
            # "libro":"...",
            # ...
            # }
            # Entonces, en lugar de pasar los parámetros uno por uno, se puede usar el dict para convertir las llaves en nombres de parámetros y sus valores como valor del parámetro usando el **
            nuevoLibro = Libro(**libroSerializado.model_dump())
            db.session.add(nuevoLibro)
            db.session.commit()

            resultado = LibroSchema.model_validate(nuevoLibro).model_dump(mode='json') # retorna la info creada del libro
            return {
                "message": "Libro agregado exitosamente",
                "content": resultado
            }, 201
        
        except ValidationError as error:
            return {
                "message": "Error al crear el libro",
                "content": error.errors()
            }, 405 


class LibroController(Resource):
    def delete(self, id):
        # Soft delete (eliminación suave) por que no se elimina el registro como tal en la BD, si no que solo cambia su estado (col eliminado)

        #Cuando modificamos las columnas que queremos obtener del ORM, esto ya no retorna como una instancia de la clase, si no que retorna como una tupla con todos los valores solicitados
        # SELECT id FROM libros WHERE id = '...' AND eliminado = false;
        # with_entities() > devuelve la columna que yo quiero
        libroEncontrado = db.session.query(Libro).with_entities(Libro.id).filter(Libro.id == id, Libro.eliminado == False).first()

        if not libroEncontrado:
            return {
                "message": "Libro no encontrado"
            }, 404

        # También se puede realizar la actualización mediante el método update
        db.session.query(Libro).filter(Libro.id == id).update({
            Libro.eliminado: True
        })

        # Guardamos la información de manera permanente en la BD
        db.session.commit()

        return {
            "message": "Libro elimnado exitosamente"
        }

    def get(self, id):
        libroEncontrado = db.session.query(Libro).filter(Libro.id == id).first()

        if not libroEncontrado:
            return {
                "message": "El libro no existe"
            }, 404

        # Gracias al relationship creado en LibroCategoria se crea el atributo virtual en la clase de Libro con el nombre colocado en el parámetro backref y cuando ingreso a este parámetro podré obtener todas sus libroCategorias pertenecientes a este libro y del mismo modo podré acceder a la categoría a la que pertenece gracias al relationship, en este caso sería categorías
        
        # print(libroEncontrado.libro_categorias)
        # print(libroEncontrado.libro_categorias[0].categoria.nombre)

        categorias = []

        for libroCategoria in libroEncontrado.libro_categorias:
            categorias.append({
                "id": libroCategoria.categoria.id,
                "nombre": libroCategoria.categoria.nombre
            })

        resultado = {
            "id": libroEncontrado.id,
            "nombre": libroEncontrado.nombre,
            # strftime > convierte una fecha a un string usando el patrón definido
            # a diferencia de strptime > convierte un string a una fecha usando el patrón de lectura
            "fechaPublicacion": datetime.strftime(libroEncontrado.fechaPublicacion, "%Y-%m-%d %H:%M:%S") if libroEncontrado.fechaPublicacion else None,
            "prologo": libroEncontrado.prologo,
            "isbn": libroEncontrado.isbn,
            "categorias": categorias
        }

        return {
            'content': resultado
        }