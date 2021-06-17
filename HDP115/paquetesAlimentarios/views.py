from django import forms
from django.http import request
from django.shortcuts import redirect, render
from principal.models import persona, paqueteAlimentario
from formulario import PaqueteForms

def indexPaquetes(request):
    paquetes = paqueteAlimentario.objects.all()
    contexto ={
        'paquetes':paquetes
    }
    return render(request,'indexPaquetes.html',contexto)

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

def eliminarPaquete(request, codigo):
    paquetes = paqueteAlimentario.objects.get(codigo = codigo)
    paquetes.delete()
    return redirect('indexPaquetes')