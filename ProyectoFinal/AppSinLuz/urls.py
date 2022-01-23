from django.urls import path
from AppSinLuz import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios', views.usuario, name='usuarios'),
    path('reclamos', views.reclamos, name='reclamos'),
    path('administrativos', views.administrativos, name='administrativos'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('contacto', views.contacto, name='contacto'),
    path('busquedaReclamo', views.busqueda_reclamo, name='busquedaReclamo'),
    path('buscar/', views.buscar, name='busqueda'),
]