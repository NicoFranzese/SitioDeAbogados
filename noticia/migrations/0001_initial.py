# Generated by Django 4.2.7 on 2023-12-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('activa', models.BooleanField(verbose_name='Activa')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
            ],
        ),
    ]