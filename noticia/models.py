from django.db import models

# Create your models here.

class Noticia(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    activa = models.BooleanField(verbose_name="Activa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificacion")
        
    def __str__(self):
        return self.title