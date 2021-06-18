from django import forms
from django.db.models.deletion import CASCADE
from django.shortcuts import redirect, render
from principal.models import asignacion 
from .form import  asignacionForm

# Create your views here.
def asignacionIndex(request):
    asignaciones = asignacion.objects.all()
    contexto = {
        'asignaciones':asignaciones
    }
    return render(request,'indexAsignacion.html',contexto)

def crearAsignacion(request):
    if request.method == 'GET':
        form = asignacionForm()
        contexto = {
            'form':form
        }
    else:
        form = asignacionForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('indexAsignacion')
    return render(request,'crearAsignacion.html',contexto)

def eliminarAsignacion(request,id):
    asigna = asignacion.objects.get(idcomprobante=id)
    asigna.delete()
    return redirect('indexAsignacion')
    