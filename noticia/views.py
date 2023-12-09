from django.shortcuts import render
from .models import Noticia

# Create your views here.
def noticia(request):
    noticias = Noticia.objects.all()
    return render(request,"noticia/noticia.html",{'noticias':noticias})