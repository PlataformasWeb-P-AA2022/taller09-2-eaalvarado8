# Generated by Django 3.2.4 on 2021-06-10 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0003_auto_20210610_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lasmatriculas', to='administrativo.estudiante'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lasmatriculas', to='administrativo.modulo'),
        ),
    ]
