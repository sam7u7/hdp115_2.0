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
from asignaciones.views import asignacionIndex, crearAsignacion, eliminarAsignacion,eliminarAsignacionIndex
from paquetesAlimentarios.views import indexPaquetes, crearPaquete, eliminar, elimiarPaquetesIndex
from principal import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuario.views import *
<<<<<<< HEAD
from login.views import *
from django.contrib.auth.views import LoginView,LogoutView
=======
from principal.views import *
>>>>>>> 067a2b53bbe3c6f4b4df0f1f96d53d393dee0055

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('asignasion/index/',asignacionIndex, name='indexAsignacion'),
    path('asignasion/crear/',crearAsignacion,name='crearAsignacion'),
    path('paquetes/index',indexPaquetes,name='indexPaquetes'),
    path('paquetes/CrearPaquetes', crearPaquete, name='crearPaquete'),
    path('asignasion/eliminar/<int:id>/',eliminarAsignacion,name = 'eliminar'),
    path('asignacion/eliminarPaquetes',eliminarAsignacionIndex,name= 'eliminarAsignacionIndex'),
    path('paquetes/eliminarPaquetes/<int:codigo>',eliminar,name='eliminarPaquete'),
    path('paquetes/eliminar',elimiarPaquetesIndex,name='eliminarPaqueteIndex'),
    path('persona/index/', inicioPersona, name = 'indexPersonas'),
    path('persona/crear/', crearPersona, name='crearPersona'),
    path('persona/editar/<int:idpersona>/', editarPersona, name='editarPersona'),
    path('persona/eliminar/<int:idpersona>', eliminarPersona, name='eliminarPersona'),
    path('usuario/registrar', registro, name='registroUsuarios'),
<<<<<<< HEAD
    path('login/register',register, name = 'registroUsuarios'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout')
=======
    path('usuario/index', inicioUsuarios, name='indexUsuarios'),
    path('entregar/entregarPaquete/<int:idEntrega>', entregar, name='entregarPaquete'),
    path('entregar/indexEntrega', entregasPaquete, name='entregasPaquete')
>>>>>>> 067a2b53bbe3c6f4b4df0f1f96d53d393dee0055
]

urlpatterns += staticfiles_urlpatterns()
