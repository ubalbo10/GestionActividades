# Generated by Django 2.1.5 on 2019-08-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_actividad_terminado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='terminado',
            field=models.BooleanField(default=False),
        ),
    ]
