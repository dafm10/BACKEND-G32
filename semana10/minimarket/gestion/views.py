from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriasView(APIView):
    # Al usar una APIView esto es muy similar al Resource de flask-restful en el cual se puede colocar los métodos HTTP como métodos de la clase
    def get(self, request):
        # en Django no se puede retornar directamente un diccionario, si no que tiene que crearse la instancia de la clase Response
        return Response(data = {
            "content": ""
        })

    def post(self, request: Request):
        print(request.data)
        serializador = CategoriaSerializer(data = request.data)
        # Si la data es válida, significa que toda la información enviada es correcta y agrega toda la info al atributo "validated_data", sin embargo si está mal, se almacenará los errores en un atributo llamado errors
        if serializador.is_valid():
            print(serializador.validated_data) # esto solo se puede llamar despues de usar el: is_valid()
            # El serializador al estar vinculado con un modelo, internamente jala la forma de guardarlo en la BD con el método SAVE
            serializador.save()

            return Response(data = {
                "message": "Categoría creada exitosamente",
                "content": serializador.data # devuelve la información de la categoría creada
            }, status = status.HTTP_201_CREATED)
        else:
            return Response(data = {
                "message": "Error al crear la categoría",
                "content": serializador.errors
            }, status = status.HTTP_400_BAD_REQUEST)