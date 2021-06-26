from django import forms
from django.db.models.deletion import CASCADE
from django.shortcuts import redirect, render
from principal.models import asignacion 
from .form import  asignacionForm
import datetime
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.db.models.functions import Coalesce

# Funcion para mostrar las asignaciones
def asignacionIndex(request):
    asignaciones = asignacion.objects.all()
    contexto = {
        'asignaciones':asignaciones
    }
    return render(request,'indexAsignacion.html',contexto)
#Funcion para crear una nueva asignacion de paquetes alimentarios
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
#Funcion para eliminar asignaciones
def eliminarAsignacion(request,id):
    asigna = asignacion.objects.get(idcomprobante=id)
    asigna.delete()
    return redirect('indexAsignacion')
#Funcion para mostrar las asignaciones a
def eliminarAsignacionIndex(request):
    asignaciones = asignacion.objects.all()
    contexto = {
        'asignaciones':asignaciones
    }
    return render(request,'eliminarAsignacion.html',contexto)

class DashboardView(TemplateView):
    template_name = 'indexAsignacion.html'
    def getCantidad():
        data=[1,2,3,4,5,6,7,8,9,10,11,12]
        
        return data

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['panel'] = 'Panel de Grafica'
        contexto['Cantidad'] = self.getCantidad()
        return contexto



    