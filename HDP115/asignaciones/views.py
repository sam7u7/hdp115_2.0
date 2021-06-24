from django import forms
from django.db.models.deletion import CASCADE
from django.shortcuts import redirect, render
from principal.models import asignacion 
from .form import  asignacionForm
import datetime
from django.http import JsonResponse

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

def eliminarAsignacionIndex(request):
    asignaciones = asignacion.objects.all()
    contexto = {
        'asignaciones':asignaciones
    }
    return render(request,'eliminarAsignacion.html',contexto)


def getCantidad(self):
    data=[]
    try:
        año = datetime.now().year
        for i in range (0,12):
            asignacion.objects.filter(fechaDeAsignacion__year=año, fechaDeAsignacion__month=i).aggregate(r=Coalsce(sum('cantidad',0)).get('r'))
            data.append(int(cantidad))
    except:
        pass
    return data

def get_context_data(self, **kwargs):
    contexto = super().get_context_data(**kwargs)
    contexto['getCantidad'] = self.getCantidad()
    return contexto



    