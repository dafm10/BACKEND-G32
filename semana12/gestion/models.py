from django.db import models
from uuid import uuid4

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()
    apellidos = models.TextField(null=True)
    sexo = models.TextField()
    correo = models.TextField(unique=True)
    password = models.TextField()

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