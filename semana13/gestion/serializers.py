from rest_framework import serializers
from .models import Jugador, Puntuacion

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class PuntuacionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Puntuacion
        fields = '__all__'