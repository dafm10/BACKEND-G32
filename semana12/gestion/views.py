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
from .serializers import UsuarioSerializer, LoginSerializer, DoctorSerializer, PacienteSerializer
from .models import Usuario, Doctor, Paciente

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
    serializador = UsuarioSerializer(instance = usuarioActual)
    return Response(data={
        "content": serializador.data
    })

@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def configurarDoctor(request: Request):
    # la info del usuario viene en request.user
    # 1. Validar si el usuario existe
    usuarioExiste = Usuario.objects.filter(id = request.user.id).first()
    if not usuarioExiste:
        return Response(data={
            "message": "El usuario no existe"
        }, status=status.HTTP_404_NOT_FOUND)
    # 2. Un usuario no puede ser doctor y paciente, entonces validar que este usuario no sea paciente, si lo es no se debe continuar
    pacienteUsuario = Paciente.objects.filter(usuario = usuarioExiste.id).first()
    if pacienteUsuario:
        return Response(data={
            "message": "El usuario ya es un paciente"
        }, status=status.HTTP_400_BAD_REQUEST)
    # 3. Guardar la información del doctor
    # Agregamos el ID del usuario proveniente del JWT a el ID del usuario que usará el doctor en el registro
    request.data['usuario'] = usuarioExiste.id
    serializador = DoctorSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()

        return Response(data={
            "message": "Doctor creado exitosamente", 
            "content": serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            "message": "Error al crear el registro",
            "content": serializador.errors
        },status=status.HTTP_400_BAD_REQUEST)
    


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def configurarPaciente(request: Request):
    usuarioExiste = Usuario.objects.filter(id = request.user.id).first()
    if not usuarioExiste:
        return Response(data={
            "message": "El usuario no existe"
        }, status=status.HTTP_404_NOT_FOUND)

    doctorUsuario = Doctor.objects.filter(usuario = usuarioExiste.id).first()
    if doctorUsuario:
        return Response(data={
            "message": "El usuario ya es un doctor"
        }, status=status.HTTP_400_BAD_REQUEST)

    request.data['usuario'] = usuarioExiste.id
    serializador = PacienteSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(data={
            "message": "Paciente creado exitosamente",
            "content": serializador.data
        },status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            "message": "Error al crear paciente",
            "content": serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)