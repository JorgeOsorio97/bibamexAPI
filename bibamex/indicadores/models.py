from django.db import models


class Indicadores(models.Model):
    nombre = models.CharField(max_length=256)
    fuente = models.CharField(max_length=256)
    g_tiempo = models.CharField(max_length=256)
    g_espacio = models.CharField(max_length=256)
    g_entidad = models.CharField(default='pais', max_length=256)
    unidad = models.CharField(null=True, max_length=256)
    data_owner = models.CharField(null=True, max_length=256)
    descripcion = models.CharField(blank=True, max_length=256)
    indicador_id = models.IntegerField(default=0)


class IndicadoresCreados(models.Model):
    nombre = models.CharField(max_length=256)
    formula_o = models.CharField(max_length=256)
    formula = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)
    descripcion = models.CharField(blank=True, max_length=256)


class Historico(models.Model):
    fecha = models.DateField()
    indicador_id = models.IntegerField()
    valor = models.FloatField()
    espacio = models.CharField(max_length=256)
    entidad = models.CharField(null=True, max_length=256)


class Transformaciones(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(blank=True, max_length=256)
