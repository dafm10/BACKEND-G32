from django.db import models
from uuid import uuid4

class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'categorias'

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.CharField(max_length=100, null=False)
    ext = models.CharField(max_length=100, null=False)
    ruta = models.CharField(max_length=200, null=False)
    # mime_type = models.CharField(max_length=100, null=False)
    mimeType = models.CharField(max_length=100, null=False, db_column='mime_type')

    class Meta:
        db_table = 'medias'

class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.CharField(max_length=100, null=False)
    disponible = models.BooleanField(default=True)
    
    media = models.ForeignKey(to=Media, on_delete=models.PROTECT, db_column='media_id')
    categoria = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, db_column='categoria_id')

    class Meta:
        db_table = "productos"


class Precio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(null=False)

    producto = models.ForeignKey(to=Producto, on_delete=models.PROTECT, db_column='producto_id')

    class Meta:
        db_table = 'precios'