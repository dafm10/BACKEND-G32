from django.urls import path
from .views import listar_recetas

# Si la variable no se llama: urlpatterns, django no podrá encontrar el conjunto de rutas declaradas y por ende no podrá ser accedidas
urlpatterns = [
    path("recetas/", listar_recetas),
]