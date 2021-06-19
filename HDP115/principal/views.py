from django.forms.models import ALL_FIELDS
from django.shortcuts import redirect, render
from principal.models import entregaPaquete
# Create your views here.

def index(request):
    return render(request,"index.html")

def entregar(request, idEntrega):
    entregar = entregaPaquete.objects.get(pk = idEntrega)
    entregarPaquetes = entregaPaquete.objects.all()
    if request.method == 'GET':
        if entregar.estado is False:
            entregar.estado = True
            entregar.save()
        contexto = {
        'entregarPaquetes' : entregarPaquetes
    }
    else:
        return redirect('indexEntrega.html')
    return render(request, 'indexEntrega.html', contexto)

def entregasPaquete(request):
    entregarPaquetes = entregaPaquete.objects.all()
    contexto = {
        'entregarPaquetes' : entregarPaquetes
    }
    return render(request, 'indexEntrega.html', contexto)