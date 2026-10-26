from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
# Vistas genéricas
# Nos brindará el proceso automático de una determinada operación
from rest_framework.generics import (CreateAPIView, # crear
                                     DestroyAPIView, # eliminar
                                     ListAPIView, # devolver todos
                                     ListCreateAPIView, # devolver todos y creación
                                     RetrieveAPIView, # devolver solo uno
                                     RetrieveDestroyAPIView, # devolver solo uno y además poder eliminar
                                     RetrieveUpdateAPIView, # eliminar y además poder actualizar
                                     RetrieveUpdateDestroyAPIView, # devolver solo uno y además poder actualizarlo o eliminarlo
                                     UpdateAPIView) # actualizar
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriasView(APIView):
    # Al usar una APIView esto es muy similar al Resource de flask-restful en el cual se puede colocar los métodos HTTP como métodos de la clase
    def get(self, request):
        categorias = Categoria.objects.all()
        # Convierte de las instancias a dict
        # Si se pasa un conjunto de instancias estamos en la obligación de colocar many=True para que el serializador pueda iterar y transformar cada una de las instancias
        dataSerializada = CategoriaSerializer(instance=categorias, many=True)
        # en Django no se puede retornar directamente un diccionario, si no que tiene que crearse la instancia de la clase Response
        return Response(data = {
            "content": dataSerializada.data
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

# GET | PUT | DELETE
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    # SELECT * FROM categorias
    # Es la forma en la cual la vista se comunicará con laBD
    queryset = Categoria.objects.all()
    
    # Es la forma en la cual la vista se comunicará con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer

    # lookup_field > sirve para indicar el parámetro que se usará para identificar la PK (llave primaria)
    lookup_field = 'id'