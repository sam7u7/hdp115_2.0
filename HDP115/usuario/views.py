from django.contrib.auth import forms
from django.shortcuts import render, redirect
from principal.models import *
from django.http import request
from .forms import *
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
            data = form.instance.rol
            
            if data == 1:
                form.save() 
                return redirect('crearAdmin') 
            else:
                form.save() 
                return redirect('crearUsuario')  
                    
    return render(request,'crearPersona.html', contexto)

#Mostrar personas A editar
def indexEditarPersona(request):
    personas = persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'indexEditarPersonas.html', contexto)

#creamos nuestra funcion para editar
def editarPersona(request, idpersona):
    personas = persona.objects.get(idpersona = idpersona)
    if request.method == 'GET':
        form4= EditarPersonaForm(instance=personas)
        contexto = {
            'form4':form4
        }
    else:
        form4 = EditarPersonaForm(request.POST, instance=personas)
        personas = persona.objects.all()
        contexto = {
            'personas': personas
        }
        if form4.is_valid():
            form4.save()
            return render(request, 'indexPersonas.html', contexto)
    return render(request, 'editarPersona.html', contexto)

#Mostrar personas A eliminar
def indexEliminarPersona(request):
    personas = persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'indexEliminarPersonas.html', contexto)

#definimos la funcion de eliminar
def eliminarPersona(request, idpersona):
    personas = persona.objects.get(idpersona = idpersona)
    personas.delete()
    return redirect ('indexEliminarPersona')

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

#creamos nuestra funcion para crear un nuevo Usuario
def crearUsuario(request):
    if request.method == 'GET':
        form2 = UsuarioForm()
        contexto={
            'form2' : form2
        }      
    else:
        form2 = UsuarioForm(request.POST)
        contexto={
            'form2' : form2
        }
        if form2.is_valid():
            form2.save()
            return redirect('indexPersonas')
                    
    return render(request,'crearUsuario.html', contexto)

#creamos nuestra funcion para crear un nuevo Administrador
def crearAdmin(request):
    if request.method == 'GET':
        form3 = AdminForm()
        contexto={
            'form3' : form3
        }      
    else:
        form3 = AdminForm(request.POST)
        contexto={
            'form3' : form3
        }
        if form3.is_valid():
            form3.save()
            return redirect('indexPersonas')
                    
    return render(request,'crearAdministrador.html', contexto)