from django.db import models
from uuid import uuid4
# AbstractUser > permite agregar nuevas columnas a la configuración inicial del auth_user (name, last_name, password, email, is_superuser, is_staff, is_active, last_login)
# AbstractBaseuser > permite modificar por completo las columnas y propiedades del auth_user
# PermissionsMixin > sirve para configurar como estará relacionada la nueva tabla de auth_user con relación a los permisos (auth_groups, auth_user_permissions)
# BaseUserManager > es el administrador sobre algunos comandos de la terminal como por ejemplo: cuando se manda a llamar al createsuperuser este manejerá ese comportamiento
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejadorUsuario(BaseUserManager):
    # Este será el método que se llamará cuando en la terminal se quiera crear un superusuario (python3 manage.py createsuperuser)
    def create_superuser(self, nombre, correo, password):
        # Validamos si el correo no está vacío
        if not correo or len(correo) == 0:
            raise ValueError("El correo es obligatorio")

        # normalize_email > quita los espacios a los laterales y pone todo en minuscula y remueve caracteres especiales como tildes u otros
        # EdUaRdo@gmail.com > eduardo@gmail.com
        correoNormalizado = self.normalize_email(correo)

        # Con esto crearemos la nueva instancia o registro del usuario
        nuevoUsuario = self.model(correo = correoNormalizado, nombre = nombre)
        # set_password > se encarga de generar el hash del password y guardarlo en la columna password
        nuevoUsuario.set_password(password)

        # Ahora modificamos los campos que usa el panel administrativo
        # is_superuser | is_staff
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True

        # Guardamos el registro en la BD
        nuevoUsuario.save()

# Vamos a usar el aut_user dentro de usuario
# Cambiamos la herencia de un modelo común y corriente al modelo encargado del auth_user
# Y también heredamos la forma en la cual se manejará los permisos del panel administrativo para el auth_user
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()
    apellidos = models.TextField(null=True)
    sexo = models.TextField()
    correo = models.TextField(unique=True)
    password = models.TextField()

    # Si aún queremos usar el panel administrativo nos vemos en la obligación de agregar estos atributos
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Este atributo servirá para indicar cual es el atributo que usaré para poder identificar al usuario al momento de hacer login en el panel administrativo
    USERNAME_FIELD = 'correo'

    # Este atributo sirve para indicar que cuando se quiera crear un superusuario en la terminal que campos se deberían solicitar
    # No se debe de colocar el mismo atributo que el username_field por que ya está implicito y asi mismo el password siempre será solicitado
    REQUIRED_FIELDS = ['nombre']

    # Modificamos el comportamiento de nuestro auth_user y le asignamos la forma de creación de un superusuario en la terminal
    objects = ManejadorUsuario()

    class Meta:
        db_table = 'usuarios'

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    colegiatura = models.TextField()
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'doctores'

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    telefono = models.TextField(null=True)
    peso = models.FloatField(null=True)
    estatura = models.FloatField(null=True)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'pacientes'

class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()

    class Meta:
        db_table = 'especialidades'

class EspecialidadDoctor(models.Model):
    # Cuando queremos crear una llave primaria compuesta en django tenemos la clase "CompositePrimaryKey" en la cual se debe colocar todas las columnas que involucrará a la creación de esa llave primaria, esto solo se debe usar cuando se usa dos o más columnas. Es clase siempre debe tener el atributo llamado pk (Primary Key)
    pk = models.CompositePrimaryKey("doctor_id", "especialidad_id")
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id')
    especialidad = models.ForeignKey(to=Especialidad, on_delete=models.PROTECT, db_column='especialidad_id')

    class Meta:
        db_table = 'especialidades_doctores'

# class EstadoCita(models.TextChoices):
#     CONFIRMADO = "CONFIRMADO", "Confirmado"
#     CANCELADO = "CANCELADO", "Cancelado"

ESTADO_CITAS = {
    # La llave será usada en la BD mientras que su valor sea mostrado en el panel administrativo, aun asi no se use el panel administrativo siempre se debe colocar ambos valores.
    "CONFIRMADO": "CONFIRMADO",
    "CANCELADO": "CANCELADO",
    "AGENDADO": "AGENDADO"
}

class Cita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    fecha = models.DateField()
    horaInicio = models.TextField(db_column='hora_inicio')
    horaFin = models.TextField(db_column='hora_fin')
    estado = models.TextField(choices=ESTADO_CITAS, default=ESTADO_CITAS['AGENDADO'])
    # estado = models.TextField(choices=EstadoCita.choices, default=EstadoCita.CONFIRMADO)
    observacion = models.TextField(null=True)
    consultorio = models.TextField(null=True)
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id')
    paciente = models.ForeignKey(to=Paciente, on_delete=models.PROTECT, db_column='paciente_id')

    class Meta:
        db_table = 'citas'