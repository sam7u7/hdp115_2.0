from types import LambdaType
from django import forms
from django import forms
from django import forms
from django.forms import widgets
from principal.models import paqueteAlimentario
#Formulario para registrar datos de paquetes alimentarios
class PaqueteForms(forms.ModelForm):
    class Meta:
        model = paqueteAlimentario
        fields = '__all__'
