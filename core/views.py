from django.shortcuts import render, HttpResponse

# Create your views here.
#def home(request):
#    html_response = "<h1>Esta es mi página principal</h1><br>"
#    for i in range(10):
#        html_response += "<h2>portada </h2>"
#    return HttpResponse(html_response)

#def about(request):
#    return HttpResponse("<h1>Sobre Nosotros</h1>")

#def portfolio(request):
#    return HttpResponse("<h1>Estos son mis Trabajos</h1>")

#def contact(request):
#    return HttpResponse("<h1>Contactate con nosotros</h1>")

def home(request):
    return render(request, "core/home.html")

def autoridades(request):
    return render(request, "core/autoridades.html")

def beneficios(request):
    return render(request, "core/beneficios.html")

def contacto(request):
    return render(request, "core/contacto.html")

def index(request):
    return render(request, "core/index.html")

def institucional(request):
    return render(request, "core/institucional.html")

def radio(request):
    return render(request, "core/radio.html")

