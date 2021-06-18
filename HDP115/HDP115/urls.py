"""HDP115 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asignaciones.views import asignacionIndex, crearAsignacion, eliminarAsignacion
from paquetesAlimentarios.views import indexPaquetes, crearPaquete, eliminar, elimiarPaquetesIndex
from principal import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('asignasion/index/',asignacionIndex, name='indexAsignacion'),
    path('asignasion/crear/',crearAsignacion,name='crearAsignacion'),
    path('paquetes/MostrarPaquetes',indexPaquetes,name='indexPaquetes'),
    path('paquetes/MostrarPaquetes/CrearPaquetes', crearPaquete, name='crearPaquete'),
    path('asignasion/eliminar/<int:id>/',eliminarAsignacion,name = 'eliminarAsignacion'),
    path('paquetes/MostrarPaquetes/<int:codigo>',eliminar,name='eliminarPaquete'),
    path('paquetes/MostrarPaquetes/eliminarPaquetes',elimiarPaquetesIndex,name='eliminarPaqueteIndex'),
    path('persona/index/', inicioPersona, name = 'indexPersonas'),
    path('persona/crear/', crearPersona, name='crearPersona'),
    path('persona/editar/<int:idpersona>/', editarPersona, name='editarPersona'),
    path('persona/eliminar/<int:idpersona>', eliminarPersona, name='eliminarPersona'),
    path('usuario/registrar', registro, name='registroUsuarios')
]

urlpatterns += staticfiles_urlpatterns()
