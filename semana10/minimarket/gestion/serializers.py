# ModelSerializer se vincula con el modelo y trae todas las configuraciones del Modelo
from rest_framework.serializers import ModelSerializer
from .models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        # Siempre debemos colocar una de los siguientes atributos, solo uno de los dos siguientes
        # fields | exclude
        # Sirve para indicar al serializador que campos (atributos) vamos a utilizar para hacer la validación
        # fields = ["id", "nombre"]
        # Pero si se va a utilizar todos los campos del modelo
        fields = "__all__"
        # Con EXCLUDE: Todos los campos, menos el nombre
        # exclude = ["nomnbre"]