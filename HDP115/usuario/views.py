from django.shortcuts import render, redirect
from principal.models import *
from django.http import request
from .forms import PersonaForm
from django.contrib.auth.forms import UserCreationForm


#creamos nuestra funcion para la lista de personas
def inicioPersona(request):
    personas = persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'indexPersonas.html', contexto)

#creamos nuestra funcion para crear una nueva persona
def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form': form
        }
    else :
        form = PersonaForm(request.POST)         
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('crearPersona')
    return render(request,'crearPersona.html', contexto)


#creamos nuestra funcion para editar
def editarPersona(request, idpersona):
    personas = persona.objects.get(idpersona = idpersona)
    if request.method == 'GET':
        form= PersonaForm(instance=personas)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance=personas)
        personas = persona.objects.all()
        contexto = {
            'personas': personas
        }
        if form.is_valid():
            form.save()
            return render(request, 'indexPersonas.html', contexto)
    return render(request, 'crearPersona.html', contexto)



#definimos la funcion de eliminar
def eliminarPersona(request, idpersona):
    personas = persona.objects.get(idpersona = idpersona)
    personas.delete()
    return redirect ('indexPersonas')

##
def registro(request):
    if request.method == 'post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            message.success(request, f'Usuario{username} creado')
    else:
        form = UserCreationForm()
    contexto= {'form': form}
    return render(request, 'registroUsuarios.html', contexto)

#creamos nuestra funcion para la lista de usuarios
def inicioUsuarios(request):
    usuarios = usuario.objects.all()
    contexto = {
        'usuarios': usuarios,
    }
    return render(request, 'indexUsuarios.html', contexto)