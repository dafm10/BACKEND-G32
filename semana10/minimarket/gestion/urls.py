from django.urls import path
from .views import CategoriasView, DevolverActualizarEliminarCategoriaView

urlpatterns = [
    # as_view convierte la vista creada con DRF a una vista que la pueda entender Django y pueda servirla
    path('categorias', CategoriasView.as_view()),
    # si le vamos a poner otro parámetro que no se llame 'id' entonces debo de modificar el looup_field indicando el mismo nombre
    path('categoria/<id>', DevolverActualizarEliminarCategoriaView.as_view())
]