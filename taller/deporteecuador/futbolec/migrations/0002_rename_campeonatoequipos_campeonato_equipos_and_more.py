# Generated by Django 4.0.5 on 2022-06-14 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CampeonatoEquipos',
            new_name='Campeonato_Equipos',
        ),
        migrations.RenameModel(
            old_name='EquipoFutbol',
            new_name='Equipo_Futbol',
        ),
    ]
