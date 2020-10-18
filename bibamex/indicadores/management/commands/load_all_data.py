import csv
from django.core.management.base import BaseCommand, CommandError

from bibamex.indicadores.models import (
    Indicadores,
    Historico
)


class Command(BaseCommand):
    help = 'Carga de datos desde un csv'

    def handle(self, *args, **options):
        root_path = "/home/jorge-valdez/Desktop/"

        indicadores_path = root_path + 'INDICADORES_TABLE.csv'
        with open(indicadores_path) as f:
            # import pdb
            # pdb.set_trace()
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if counter == 0:
                    counter += 1
                    continue
                _, created = Indicadores.objects.get_or_create(
                    indicador_id=row[0],
                    nombre=row[1],
                    fuente=row[2],
                    g_tiempo=row[3],
                    g_espacio=row[4],
                    g_entidad=row[5],
                    unidad=row[6],
                    data_owner=row[7]
                )
                counter += 1
        historico_path = root_path + 'historico.csv'
        with open(historico_path) as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if counter == 0:
                    counter += 1
                    continue
                _, created = Historico.objects.get_or_create(
                    fecha=row[0],
                    indicador_id=row[1],
                    valor=row[2] if row[2] != '' else 0,
                    espacio=row[3],
                    entidad=row[4]
                )
                counter += 1
