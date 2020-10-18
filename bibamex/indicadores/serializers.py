from rest_framework.serializers import ModelSerializer
from bibamex.indicadores.models import Indicadores
from bibamex.indicadores.models import IndicadoresCreados
from bibamex.indicadores.models import Transformaciones


class IndicadoresSerializer(ModelSerializer):

    class Meta:
        model = Indicadores
        fields = ('id', 'nombre', 'fuente', 'g_tiempo', 'g_espacio', 'indicador_id', 'descripcion')


class IndicadoresCreadosSerializer(ModelSerializer):

    class Meta:
        model = IndicadoresCreados
        fields = ('id', 'nombre', 'formula_o', 'formula', 'tipo', 'descripcion')


class TransformacionesSerializer(ModelSerializer):

    class Meta:
        model = Transformaciones
        fields = ('id', 'nombre', 'descripcion')
