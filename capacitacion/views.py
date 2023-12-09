from django.shortcuts import render
from .models import Capacitacion

# Create your views here.
def capacitacion(request):
    capacitaciones = Capacitacion.objects.all()
    return render(request,"capacitacion/capacitacion.html",{'capacitaciones':capacitaciones})