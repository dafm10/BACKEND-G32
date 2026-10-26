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
from rest_framework.viewsets import ViewSet
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriasView(APIView):
    # Al usar una APIView esto es muy similar al Resource de flask-restful en el cual se puede colocar los métodos HTTP como métodos de la clase
    def get(self, request):
        # SELECT * FROM categorias WHERE eliminado = FALSE;
        categorias = Categoria.objects.filter(eliminado = False).all()
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

# Vistas genéricas > útiles en el caso de que no tengamos lógica
# GET | PUT | DELETE
# si mi vista genérica deja de ser genérica, entonces la puedo convertir en un "viewset" en el cual
# post > create
# get > retrieve
# get > list (si se va a retornar varios registros)
# put > update
# delete = destroy
# patch > partial_update
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    # SELECT * FROM categorias
    # Es la forma en la cual la vista se comunicará con laBD
    queryset = Categoria.objects.all()
    
    # Es la forma en la cual la vista se comunicará con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer

    # lookup_field > sirve para indicar el parámetro que se usará para identificar la PK (llave primaria)
    lookup_field = 'id'

    # Devolver solo una categoría
    def retrieve(self, request, id):
        # Al usar el retrieve | update | destroy, siempre lo enviará como 2do parámetro
        categoriaEncontrada = Categoria.objects.filter(eliminado = False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "La categoría no existe"
            }, status=status.HTTP_404_NOT_FOUND)
        
        dataSerializada = self.serializer_class(instance = categoriaEncontrada)
        
        return Response(data={
            "content": dataSerializada.data
        })

    def update(self, request, id):
        categoriaEncontrada = Categoria.objects.filter(eliminado = False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "La categoría no existe"
        }, status=status.HTTP_404_NOT_FOUND)

        serializador = self.serializer_class(data = request.data)
        if serializador.is_valid():
            serializador.update(categoriaEncontrada, serializador.validated_data)

            return Response(data={
                "message": "Categoría actualizada exitosamente",
                "content": serializador.data
            })
        else:
            return Response(data={
                "messsage": "Error al actualizar la categoría",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, id):
        categoriaEncontrada = Categoria.objects.filter(eliminado = False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "La categoría no existe"
        }, status=status.HTTP_404_NOT_FOUND)

        # Cambiamos el estado de eliminado a verdadero
        categoriaEncontrada.eliminado = True
        categoriaEncontrada.save()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT) # 204 significa que el cliente no va a leer nada


class ProductosView(ViewSet):
    def create(self, request: Request):
        serializador = ProductoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()

            return Response(data={
                "message": "Producto creado exitosamente",
                "content": serializador.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message": "Error al crear el producto",
                "content": serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        pass