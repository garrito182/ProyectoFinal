import email
from django.shortcuts import render, redirect
from django.http import HttpResponse, request



from AppSinLuz.models import Administrativo, Reclamo, Usuario
# Create your views here.

def inicio(request):
    
    return render(request, 'AppSinLuz/inicio.html')

def usuario(request):
    
    return render(request, "AppSinLuz/registrarse.html")

def reclamos(request):
    
    return render(request, 'AppSinLuz/reclamos.html')

def reclamos(request):
    
    if request.method == "POST":
       fecha = request.POST['fecha']
       detalles = request.POST['detalles']
       print(request.POST)
       Reclamo.objects.create(fecha=fecha,descripcion=detalles)
       return render(request, 'AppSinLuz/inicio.html')
    
    return render(request, 'AppSinLuz/reclamos.html')

def administrativos(request):
    
    return render(request, 'AppSinLuz/administrativos.html')

def administrativos(request):
    
    if request.method == "POST":
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        print(request.POST)
        Administrativo.objects.create(usuario=usuario,contrasena=contrasena)
        return render(request, 'AppSinLuz/inicio.html')
    
    return render(request, 'AppSinLuz/administrativos.html')

def registrarse(request):

    return render(request, 'AppSinLuz/registrarse.html')

def registrarse(request):
    
    if request.method == "POST":
       usuario = request.POST['usuario']
       contrasena = request.POST['contrasena']
       email = request.POST['email']
       direccion = request.POST['direccion']
       departamento = request.POST['departamento']
       print(request.POST)
       Usuario.objects.create(usuario=usuario,contrasena=contrasena,email=email,direccion=direccion,departamento=departamento)
       return render(request, 'AppSinLuz/inicio.html')
    return render(request, 'AppSinLuz/registrarse.html')


def contacto(request):

    return render(request, 'AppSinLuz/contacto.html')


def busqueda_reclamo(request):
    
    return render(request, 'AppSinLuz/busquedaReclamo.html')

def buscar(request):
    
    if request.method == "GET":
        fecha = request.GET['fecha']
        reclamos = Reclamo.objects.filter(fecha=fecha)
        return render(request, 'AppSinLuz/buscar.html', {'reclamos':reclamos, 'fecha':fecha})
    else:
        
        respuesta = "No ingreso una fecha."
    return HttpResponse(respuesta)