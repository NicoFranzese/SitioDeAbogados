from django.db import models

# Create your models here.

class Capacitacion(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    fecha_desde = models.DateField(null=True, verbose_name="Fecha Desde")
    fecha_hasta = models.DateField(null=True, verbose_name="Fecha Hasta")
    activa = models.BooleanField(verbose_name="Activa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificacion")
        
    def __str__(self):
        return self.title