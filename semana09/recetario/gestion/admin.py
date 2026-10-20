from django.contrib import admin
from .models import Ingrediente, Preparacion, Receta

# Acá se declaran todos los modelos que pueden ser accedidos desde el panel administrativo
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "cantidad", "recetaId"]
    # Cuando se quiere buscar una FK no se puede declarar directamente si no que se tiene que usar su referencia al modelo adyacente
    # Al momento de referenciar al modelo de la FK se pone el nombre de la FK y luego el doble sub guión y luego el nombre de la columna que queremos buscar
    search_fields = ["descripcion", "recetaId__titulo"]

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    # Que columnas puedo visualizar en la lista
    list_display = ["id", "titulo", "descripcion", "habilitado"]
    # Opciones de filtros de las columnas en la barra lateral
    list_filter = ["habilitado"]
    # Al definir se hará la búsqueda en las columnas declaradas
    search_fields = ["titulo", "descripcion"]
    # Permite editar campos en la lista sin la necesidad de ingresar a su detalle
    list_editable = ["habilitado"]
    # Modifica el ordenamiento predeterminado o indicado en el modelo en el panel administrativo
    ordering = ["titulo"]
    # bloque la edición de determinados campos
    # readonly_fields = ["titulo"]

@admin.register(Preparacion)
class PreparacionAdmin(admin.ModelAdmin):
    pass