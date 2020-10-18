from django.contrib import admin

from bibamex.indicadores.models import (
    Indicadores,
    IndicadoresCreados,
    Historico,
    Transformaciones
)


@admin.register(Indicadores)
class IndicadoresAdmin(admin.ModelAdmin):
    pass


@admin.register(IndicadoresCreados)
class IndicadoresCreadosAdmin(admin.ModelAdmin):
    pass


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    pass


@admin.register(Transformaciones)
class TransformacionesAdmin(admin.ModelAdmin):
    pass
