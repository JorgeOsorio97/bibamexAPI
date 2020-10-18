from django.urls import path
from rest_framework.routers import DefaultRouter

from bibamex.indicadores.views import (
    IndicadoresUser,
    IndicadoresCreadosUser,
    TranformacionesUser,
)

app_name = "indicadores"
router = DefaultRouter()
urlpatterns = router.urls

