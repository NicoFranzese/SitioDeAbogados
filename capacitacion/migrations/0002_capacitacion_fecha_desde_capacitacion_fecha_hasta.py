# Generated by Django 4.2.7 on 2023-12-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitacion',
            name='fecha_desde',
            field=models.DateField(null=True, verbose_name='Fecha Desde'),
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='fecha_hasta',
            field=models.DateField(null=True, verbose_name='Fecha Hasta'),
        ),
    ]
