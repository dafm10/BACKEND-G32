from django.db import models
from uuid import uuid4

class Receta(models.Model):
    # https://docs.djangoproject.com/en/6.1/topics/db/models/
    id = models.AutoField(primary_key=True, null=False)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        # Es un método de las clases de python que sirve para modificar la forma en la cual se representará la instancia
        return self.titulo

    class Meta:
        # SIEMPRE SE LLAMA META por que en los modelos se usa para poder modificar las propiedades del modelo como. su nombre de la tabla, ordenamiento
        # Metatributes
        # https://docs.djangoproject.com/en/6.1/ref/models/options/
        db_table = 'recetas'
        # si se quiere el ordenamiento de manera asc entonces se le pone el atributo
        # y si se quiere de manera descendente se pone al comienzo un guión '-'
        ordering = ['titulo']
        # CONSTRAINTS = sirve para poder indicar una unicidad en conjunto, es decir
        # constraints = [['titulo', 'descripción'], ['titulo', 'habilitado']]

class Ingrediente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    descripcion = models.TextField(null=False)
    cantidad = models.TextField(null=False)
    # Llaves foráneas
    # on_delete y el on_update > esto se usa para las relaciones y sirven para indicar cual será el comportamiento de la llave foránea cuando el padre sea eliminado.
    # Elementos:
    ## CASCADE > Si el padre es eliminado, automáticamente los hijos son eliminados. Si la receta se elimina, se eliminan todos los ingredientes de manera automática
    ## PROTECT > Evita la eliminación del padre si tiene hijos. Si se quiere eliminar una receta que tiene ingredientes no se podrá
    ## RESTRICT > Igual que el PROTECT solo que emite una excepción de RESTRICT_VALUE_ERROR
    ## SET_DEFAULT > Se puede colocar un valor por defecto si se elimina el padre. Si se elimina la receta cambiará la FK a un valor por defecto (puede ser otro padre)
    ## DO_NOTHING > ES EL PEOR DE TODOS!. No hace nada y permite la eliminación del padre y el hijo seguirá conservando su ID. Si se elimina la receta, el ingrediente seguirá conservando su ID que ya no existe y generará desintegridad de datos
    ## SET_NULL > Permite la eliminación del padre y cambia el valor de la FK a null. Si se elimina el padre los ingredientes la receta_id cambiará a NULL
    recetaId = models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table = 'ingredientes'

class Preparacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    descripcion = models.TextField()
    orden = models.IntegerField(null=False)
    recetaId = models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table = 'preparaciones'
        # Unicidad en conjunto indicando que el orden y la recetaId no se puede repetir
        # orden | recetaId
        #   1   |   1
        #   2   |   1
        #   1   |   2
        #   2   |   1 [X]
        # https://docs.djangoproject.com/en/6.1/ref/models/options/#unique-together
        unique_together = [['orden', 'recetaId']]
        # Sirve para modificar el nombre pluralizado que se mostrará SOLAMENTE en la panel administrativo
        verbose_name_plural = 'Preparaciones'