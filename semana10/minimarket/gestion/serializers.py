# ModelSerializer se vincula con el modelo y trae todas las configuraciones del Modelo
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
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

class GenerarUrlAWSSerializer(Serializer):
    # Crearemos manualmente todas las columnas a validar
    # https://www.iana.org/assignments/media-types
    # https://www.django-rest-framework.org/api-guide/fields/
    contentTypeValidas = ["image/jpeg", "image/png", "application/pdf"]
    extensionesValidas = ["png", "jpg", "jpeg", "pdf"]

    # trim_whitespace > Remueve los espacios al comienzo y al final
    fileName = serializers.CharField(trim_whitespace=True, max_length=100, required=True)
    ext = serializers.ChoiceField(choices=extensionesValidas, error_messages={"invalid_choice":"Extensión inválida, use 'image/jpeg', 'image/png' ó 'application/pdf'"}, required=True)
    contentType = serializers.ChoiceField(choices=contentTypeValidas, required=True)
    # El tamaño máximo permitido y este deberá ser enviado en bytes
    # 1 byte x 1024 > 1 kb x 1024 > 1 mb x 1024 > 1 gb x 1024 > 1 tb
    # El valor máximo 10mb y el mínimo 5kb
    size = serializers.FloatField(max_value=10*1024*1024, min_value= 5*1024, required=True)
    folder = serializers.CharField(required=False)