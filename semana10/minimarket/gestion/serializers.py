# ModelSerializer se vincula con el modelo y trae todas las configuraciones del Modelo
from rest_framework.serializers import ModelSerializer
from .models import Categoria, Producto

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        # Siempre debemos colocar una de los siguientes atributos, solo uno de los dos siguientes
        # fields | exclude
        # Sirve para indicar al serializador que campos (atributos) vamos a utilizar para hacer la validación
        # fields = ["id", "nombre"]
        # Pero si se va a utilizar todos los campos del modelo
        # fields = "__all__"
        # Con EXCLUDE: Todos los campos, menos el nombre
        exclude = ["eliminado"]


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]

class ProductoDetalleSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]
        # Podemos acceder a la información que está adyacente a este mdoelo, es decir, si se pone 1 ingresaremos 1 nivel y si ponemos 2 ingresamos 2 niveles (si hay)
        depth = 1