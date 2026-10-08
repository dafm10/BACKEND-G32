from flask_restful import Resource, request
from app.extensions import db
from app.schemas import RegistroUsuarioSchema, LoginUsuarioSchema, UsuarioSchema
from app.models import Usuario
from pydantic import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from jwt import encode
# from os import getenv
from datetime import timedelta

class RegistroController(Resource):
    def post(self):
        try:
            dataValidada = RegistroUsuarioSchema.model_validate(request.get_json())
            print(dataValidada)
            # Buscar si hay algún usuario que ya exista con este correo
            # with_entities muestras las columnas consultadas
            # SELECT id FROM usuario WHERE correo = "...";
            usuarioExistente = db.session.query(Usuario).with_entities(Usuario.id).filter(Usuario.correo == dataValidada.correo).first()

            if usuarioExistente:
                return {
                    'message': 'Usuario ya existe'
                },400

            # Proceso del hashing de la password
            # 1. Generamos el texto de ayuda (salt)
            salt = gensalt()
            
            # 2. Convertimos el password a bytes
            # password = bytes(dataValidada.password.encode())
            password = dataValidada.password.encode()

            # 3. Hacemos el hashing de la password
            password_hasheada_bytes = hashpw(password, salt)

            # 4. Convertimos el hashing del password en bytes a str
            password_hasheada = password_hasheada_bytes.decode()

            # TODO ESTE PROCESO SE PUEDE RESUMIR EN UN SOLO PASO
            # password_hasheada = hashpw(dataValidada.password.encode(),gensalt()).decode()
            
            print(password_hasheada)
            # nuevoUsuario = Usuario(correo = dataValidada.correo, password = password_hasheada, nombre = dataValidada.nombre, apellido = dataValidada.apellido)

            # Podemos usar la información de la validación directamente de forma más resumida
            # Ahora convertido la información validada a diccionario procedemos a quitar la propiedad password
            nuevoUsuario = Usuario(**dataValidada.model_dump(exclude=("password")), 
            # Para luego agregarla como parámetro a la clase
            password=password_hasheada
            )

            db.session.add(nuevoUsuario)
            db.session.commit()

            return {
                'message': 'Usuario registrado exitosamente'
            }, 201
        
        except ValidationError as error:
            print(error.errors())
            return {
                'message': 'Error al crear el usuario',
                # El context brinda información adicional sobre el error que se está dando, muchas veces acá se almacena la instancia de nuestro error, entonces para no mostrarlo cuando se envia al cliente, se quita con el método include_context en False
                'content': error.errors(include_context=False)
            }, 400


class LoginController(Resource):
    def post(self):
        try:
            dataValidada = LoginUsuarioSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 404
            #Convertimos tanto la password como la password hasheada a bytes
            password = dataValidada.password.encode()
            hashedPassword = usuarioEncontrado.password.encode()

            # checkpw sirve para que usando el hashing almacenado en la BD me diga si es o no es la password sin la necesidad de saber el valor inicial
            esLaPassword = checkpw(password,hashedPassword)

            if esLaPassword:
                # encode({"id": usuarioEncontrado.id}, getenv('JWT_KEY'))
                jwt = create_access_token(identity=usuarioEncontrado.id, # Es el identificador de la jwt, a quien le pertenece
                                    # para mantener la sesión activa y mantenga la token, en este caso es solo token de acceso
                                    fresh=False,  # Si queremos que esta JWT sea usada como un refresh jwt
                                    expires_delta=timedelta(hours=8, minutes=5)) # Indica la duración que tendrá de validez la JWT
                return {
                    'content': jwt
                }
            else:
                return {
                    'meesage':'Credenciales incorrectas'
                }, 404
    
        except ValidationError as error:
            return {
                'message':'Error al hacer el login',
                'content':error.errors(include_context=False)
            }

class UsuarioController(Resource):
    @jwt_required() # Sirve para indicar que el método que va a tratar de acceder tenga de manera OBLIGATORIA la JWT si no será rechazado
    def get(self):
        id = get_jwt_identity() # Devolvrá el identificador de la JWT, es decir el valor contenido en JTI dentro del playload

        usuarioEncontrado = db.session.query(Usuario).filter(Usuario.id == id).first()

        # Pasamos la instancia del usuario encontrado y con model_dump devuelve el diccionario en formato json
        resultado =  UsuarioSchema.model_validate(usuarioEncontrado).model_dump(mode='json')

        return {
            'content': resultado
        }