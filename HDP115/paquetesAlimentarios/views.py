from django import forms
from django.http import request
from django.shortcuts import redirect, render
from principal.models import paqueteAlimentario
from .formulario import PaqueteForms

#Funcion creada para mostrar listado de personas
def indexPaquetes(request):
    paquetes = paqueteAlimentario.objects.all()
    contexto ={
        'paquetes':paquetes
    }
    return render(request,'indexPaquetes.html',contexto)
#Funcion creada para registrar y crear un nuevo paquete en un formulario
def crearPaquete(request):
    if request.method == 'GET':
        form = PaqueteForms()
        contexto ={
            'form':form
        }
    else: 
        form = PaqueteForms(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('indexPaquetes')
    return render(request, 'crearPaquete.html', contexto)
#Funcion creada para eliminar
def eliminar(request, codigo):
    paquetes = paqueteAlimentario.objects.get(codigo = codigo)
    paquetes.delete()
    return redirect('eliminarPaqueteIndex')
#Funcion creada para mostrar los paquetes que se pueden eliminar
def elimiarPaquetesIndex(request):
    paquetes = paqueteAlimentario.objects.all()
    contexto ={
        'paquetes':paquetes
    }
    return render(request,'eliminarPaquete.html',contexto)