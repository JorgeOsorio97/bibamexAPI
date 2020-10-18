from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IndicadoresConfig(AppConfig):
    name = "bibamex.indicadores"
    verbose_name = _("indicadores")

    