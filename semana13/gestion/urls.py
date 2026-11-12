# https://www.django-rest-framework.org/api-guide/routers/
from rest_framework import routers
from .views import JugadorApiView, PuntuacionApiView

router = routers.SimpleRouter()
router.register('jugadores', JugadorApiView, basename='jugadores')
router.register('puntuaciones', PuntuacionApiView, basename='puntuaciones')

urlpatterns = router.urls