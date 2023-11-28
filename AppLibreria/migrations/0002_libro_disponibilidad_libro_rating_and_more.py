# Generated by Django 4.2.7 on 2023-11-28 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='disponibilidad',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('prestado', 'Prestado'), ('en_proceso', 'En_Proceso')], default='disponible', max_length=20),
        ),
        migrations.AddField(
            model_name='libro',
            name='rating',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='estadoPrestamo',
            field=models.CharField(choices=[('prestado', 'Prestado'), ('devuelto', 'Devuelto')], default='prestado', max_length=20),
        ),
    ]
