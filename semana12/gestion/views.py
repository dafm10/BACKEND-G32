from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (IsAuthenticated, # Obligará a que si no hay una token y esta sea válida, no permitirá ingresar al EndPoint
                                        IsAdminUser, # vaidará que el usuario que quiera consultar sea is_superuser y si no no podrá continuar
                                        IsAuthenticatedOrReadOnly, # Validará que si el método es GET normal podrá continuar, pero si no es GET la token será obligatoria y tiene que ser válida
                                        AllowAny # Permitirá que cualquiera pueda consultar cualquier método, sin la necesidad de enviar una token, esto es el valor prederterminado
                                        )
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import UsuarioSerializer, LoginSerializer
from .models import Usuario

@api_view(http_method_names=['POST'])
def registroUsuario(request: Request):
    serializador = UsuarioSerializer(data = request.data)

    if serializador.is_valid():
        print(serializador.validated_data)
        nombre = serializador.validated_data.get('nombre')
        correo = serializador.validated_data.get('correo')
        sexo = serializador.validated_data.get('sexo')
        password = serializador.validated_data.get('password')
        nuevoUsuario = Usuario(nombre = nombre, correo = correo, sexo = sexo)

        # El modelo auth_user tiene un método set_password que genera el hash de la contraseña y lo guarda en el campo de password
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()

        return Response(data={
            "messasge": "Usuario registrado exitosamente"
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            "message": "Error al crear el usuario",
            "content": serializador.errors
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
def loginManual(request: Request):
    serializador = LoginSerializer(data = request.data)
    
    if serializador.is_valid():
        correo = serializador.validated_data.get('correo')
        password = serializador.validated_data.get('password')
        usuarioEncontrado = Usuario.objects.filter(correo = correo).first()
        # Acá se deberían agregar mas filtros: si está habilitado, si tiene los permisos necesarios, etc.
        if not usuarioEncontrado:
            return Response(data={
                "message": "El usuario no existe",
            }, status=status.HTTP_400_BAD_REQUEST)

        # Este método es propio del auth_user que al heredar en la case de usuario podemos utilizarlo
        esLaPassword = usuarioEncontrado.check_password(password)
        if esLaPassword:
            # Para generar tokens necesito llamar a la clase RefreshToken y esta me retornará tokens de acceso y de refrescopara la sesión
            # Podemos usar cualquiera de las 2 formas de devolver el token (token o token2)
            token = RefreshToken.for_user(usuarioEncontrado)
            token2 = AccessToken.for_user(usuarioEncontrado)
            return Response(data={
                "content":{
                    "accessToken": str(token.access_token)
                },
                "token": str(token2)
            })
        else:
            return Response(data={
                "message": "Credenciales inválidas",
            },status=status.HTTP_403_FORBIDDEN)
    else: 
        return Response(data={
            "message": "Error al hacer el login",
            "content": serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# DRF tiene un formato de poder requerir o no la autenticación en los métodos que sea necesario mediante el decorador: permission_classes, o dentro de las vistas usando el atributo: permissions_classes
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def perfilUsuario(request: Request):
    print(request.auth) # retorna la JWT directa
    print(request.user) # retorna la instancia que le pertenece al usuario

    usuarioActual = request.user

    return Response(data={
        "content": ""
    })