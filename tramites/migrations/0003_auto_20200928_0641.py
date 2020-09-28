# Generated by Django 3.1.1 on 2020-09-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramites', '0002_tramite_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramite',
            name='tramite',
            field=models.CharField(choices=[('DONACION', 'Donación'), ('SUCESION', 'Sucesión'), ('ACT_DATO', 'Actualización datos'), ('SUGE_CIA', 'Sugerencias')], max_length=8),
        ),
    ]
