# Ahora todos los métodos (GET, POST, PUT, DELETE), se definirán como métodos de una clase
from flask_restful import Resource

class CategoriaController(Resource):
    def get(self):
        return {
            "message": "Las categorías son:"
        } # Su código de estado por defecto es 200

    def post(self):
        return {
            "message": "Categoría creada exitosamente"
        }, 201 # Created