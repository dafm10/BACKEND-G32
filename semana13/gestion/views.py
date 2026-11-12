# https://www.django-rest-framework.org/api-guide/generic-views/
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import JugadorSerializer, PuntuacionSerialier
from .models import Jugador, Puntuacion
from django.core.cache import cache

# Si queremos usar el enrutador de DRF este solamente va funcionar con los viewsets o con los APIViews, más no funcionará con los generics views
# https://www.django-rest-framework.org/api-guide/viewsets/
class JugadorApiView(ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()

class PuntuacionApiView(ModelViewSet):
    serializer_class = PuntuacionSerialier
    queryset = Puntuacion.objects.all()

    # El decorador @action permite agregar endpoints personalizados dentro de un Viewset 
    # para acceder a este enpoint tenemos que agregar la sub-url/ranking al final ya que estamos agregando un nuevo endpoint en lugar de modificar el retrieve o list propios del Viewset
    @action(detail=False, methods=['GET'])
    def ranking(self, request: Request):
        # Primero obtengo la data desde el Redis en vez de ir a la BD
        data = cache.get('ranking_top10')
        if data is None:
            print("Está vacio la caché")
            # En el order_by se puede ordenar ascendentemente solo colocando el nombre de la propiedad pero si se quiere ordenar descendentemente entonces al comienzo se le pone un guión (-)
            # En el ORM de Django no hay limit ni offset, si no que se coloca como si fuese posición de una lista, y eso al hacer la consulta en la BD se hace la paginación correspondiente (se agrega el limit y el offset si es necesario)
            # SELECT score, nombre 
            # FROM puntuaciones AS p INNER JOIN jugadores AS j ON p.jugador_id = j.id 
            # LIMIT 10 
            # ORDER BY score DESC;
            nuevaData = list(Puntuacion.objects.order_by('-score').values('jugador__nombre', 'score')[:10])
            # Guardaré la nueva información proveniente de la BD de postgres en mi BD de Redis con un tiempo de espera máximo de 30s, si no lanzará un error
            # El parámetro timeout sirve para indicar cuanto tiempo va a durar en la BD la redis esta inforamación, luego de ese tiempo automáticamente será eliminada para evitar mostrar información pasada que ya no es relevante
            cache.set('ranking_top10', nuevaData, timeout=60)

        return Response(data)