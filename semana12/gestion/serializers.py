from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_staff', 'is_superuser', 'is_active'] # estos son del panel administrativo, en caso lo usemos, lo quitamos de exclude


class LoginSerializer(Serializer):
    correo = EmailField(required = True)
    password = CharField(required = True)