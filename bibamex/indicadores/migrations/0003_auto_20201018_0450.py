# Generated by Django 3.0.10 on 2020-10-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0002_indicadores_indicador_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadores',
            name='unidad',
            field=models.CharField(max_length=256, null=True),
        ),
    ]