from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from bibamex.users.api.views import UserViewSet

from bibamex.indicadores.views import (
    IndicadoresUser,
    IndicadoresCreadosUser,
    TranformacionesUser,
    ListHistoricos,
)


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
router.register(r'Indicadores', IndicadoresUser, basename='indicadores')
router.register(r'IndicadoresCreados', IndicadoresCreadosUser, basename='indicadores')
router.register(r'Transformaciones', TranformacionesUser, basename='indicadores')

urlpatterns = [path('', include(router.urls)),
               path('Historicos/', ListHistoricos.as_view())]
