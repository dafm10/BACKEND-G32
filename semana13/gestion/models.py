from django.db import models
from uuid import uuid4

class Jugador(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.TextField()

    class Meta:
        db_table = 'jugadores'

class Puntuacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    score = models.IntegerField()
    jugador = models.ForeignKey(to=Jugador, on_delete=models.PROTECT, db_column='jugador_id')

    class Meta:
        db_table = 'puntuaciones'