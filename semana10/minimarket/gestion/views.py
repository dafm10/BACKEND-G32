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
from rest_framework.decorators import api_view # en caso solo querramos usar un método en particular
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, ProductoDetalleSerializer, GenerarUrlAWSSerializer
from uuid import UUID
from os import getenv
from boto3 import client
from urllib.parse import unquote # para hacer que la url enviada por AWS no sea modificada en bruno o urls que queremos devolver desde django

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
        # Validar si la categoría enviada no ha sido eliminada, si esta eliminada entonces no proceder con la creación del producto
        categoriaEncontrada = Categoria.objects.filter(id = request.data.get("categoria"), eliminado = False).first()

        if not categoriaEncontrada:
            return Response(data={
                "message": "Error al crear el producto",
                "content": "Categoría no existe"
            },status=status.HTTP_400_BAD_REQUEST)

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

    def list(self, request: Request):
        # Al usar el get en un query_params solamente retornará la primera información del query_param, es decir, si se envia una lista de varios valores, solamente tomará el primero, en cambio el getlist obtiene todos los valores y los retorna en formato de lista, para poder ser iterables
        categoria = request.query_params.getlist('categoria')
        nombre = request.query_params.get('nombre')

        filtros = {
            "eliminado": False
        }
        if categoria:
            # https://docs.djangoproject.com/en/6.1/ref/models/querysets/#field-lookups
            filtros["categoria__in"] = []

            for categoriaId in categoria:
                # Acá hacemos la validación si el id de la categoría es UUID válido, para evitar algún error pero del lado de la BD
                try:
                    UUID(categoriaId)
                except:
                    return Response(data={
                        "message": f"El id de la categoría {categoriaId} es inválido"
                    })
                
                categoriaEncontrada = Categoria.objects.filter(id = categoriaId, eliminado = False).first()
                if categoriaEncontrada:
                    filtros["categoria__in"].append(str(categoriaEncontrada.id))
            
            # Validamos que si al final todas las categorías enviadas no existen entonces no agregamos ese filtro a la variable
            if len(filtros["categoria__in"]) == 0:
                del filtros["categoria__in"]

        if nombre:
            # en SQL al usar el % en una búsqueda de LIKE o ILIKE estamos indicando que nos interesa que caracteres vienen antes o vienen despupés
            # icontains > es en SQL un ILIKE
            filtros["nombre__icontains"] = nombre

        print(filtros)
        # al usar el ** en un método y ese sea un diccionario estos indican que las llaves del diccionario se convierten a parámetro y sus valores se convertirán a valores de los parámetros, es decir data= {"nombre": "Eduardo"} > **data > (nombre="Eduardo")
        productos = Producto.objects.filter(**filtros).all()
        serializador = ProductoSerializer(instance=productos, many=True)
        return Response(data = {
            "content": serializador.data
        })


class ProductoView(ViewSet):
    def retrieve(self, request: Request, id):
        productoEncontrado = Producto.objects.filter(id = id, eliminado = False).first()
        if not productoEncontrado:
            return Response(data={
                "message": "Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        
        serializador = ProductoDetalleSerializer(instance = productoEncontrado)

        return Response(data={
            "content": serializador.data
        })

    def destroy(self, request: Request, id):
        productoEncontrado = Producto.objects.filter(id = id, eliminado = False).first()
        
        if not productoEncontrado:
            return Response(data={
                "message": "Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        # Realizamos el soft-delete cambiando el estado del eliminado del producto a True y lo guardamos en la BD
        productoEncontrado.eliminado = True
        productoEncontrado.save()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST'])
def crearUrlParaSubirArchivo(request: Request):
    # https://docs.aws.amazon.com/boto3/latest/guide/s3-presigned-urls.html
    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/generate_presigned_url.html
    serializador = GenerarUrlAWSSerializer(data=request.data)
    if serializador.is_valid():
        fileName = serializador.validated_data.get("fileName")
        ext = serializador.validated_data.get("ext")
        contentType = serializador.validated_data.get("contentType")
        folder = serializador.validated_data.get("folder", "/")

        s3 = client('s3')
        
        url = s3.generate_presigned_url(
            ClientMethod = 'put_object',
            Params ={
                "Bucket":getenv('BUCKET_NAME'),
                "Key": folder + fileName + ext,
                "ContentType": contentType
            },
            ExpiresIn=150
        )
        return Response(data={
            "content": unquote(url)
        })
    else:
        return Response(data={
            "message": "Error al generar la URL",
            "content": serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)