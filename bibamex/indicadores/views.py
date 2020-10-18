import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import django_filters
from bibamex.indicadores.models import Indicadores
from bibamex.indicadores.models import IndicadoresCreados
from bibamex.indicadores.models import Transformaciones
from bibamex.indicadores.models import Historico

from bibamex.indicadores.serializers import IndicadoresSerializer
from bibamex.indicadores.serializers import IndicadoresCreadosSerializer
from bibamex.indicadores.serializers import TransformacionesSerializer


class IndicadoresUser(ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['g_espacio', 'g_entidad']
    serializer_class = IndicadoresSerializer
    queryset = Indicadores.objects.all()


class IndicadoresCreadosUser(ModelViewSet):
    serializer_class = IndicadoresCreadosSerializer
    queryset = IndicadoresCreados.objects.all()


class TranformacionesUser(ModelViewSet):
    serializer_class = TransformacionesSerializer
    queryset = Transformaciones.objects.all()


class ListHistoricos(APIView):
    def post(self, request, format=None):
        print(request.data['indicadores'])
        res = []
        for i in request.data['indicadores']:
            name = Indicadores.objects.get(indicador_id=i).nombre
            temp = Historico.objects.filter(indicador_id=i)
            print(type(temp[0].fecha))
            res.append({
                'nombre': name,
                'data': [[x.fecha, x.valor] for x in temp]
            })
        return Response(res)
