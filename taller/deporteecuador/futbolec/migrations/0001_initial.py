# Generated by Django 4.0.5 on 2022-06-14 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de Campeonato')),
                ('nombre_auspiciante', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de Equipo')),
                ('siglas', models.CharField(max_length=30)),
                ('userTwitter', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de Jugador')),
                ('posicion', models.CharField(choices=[('1', 'Arquero'), ('2', 'Centro'), ('3', 'Delantero'), ('4', 'Defensa')], max_length=30)),
                ('numero_camisa', models.IntegerField(verbose_name='Numero Camiseta')),
                ('sueldo', models.IntegerField(verbose_name='sueldo')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losjugadores', to='futbolec.equipofutbol')),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='a??o')),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elcampeonato', to='futbolec.campeonato')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.equipofutbol')),
            ],
        ),
    ]
