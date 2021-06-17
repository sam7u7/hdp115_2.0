from django import forms
from django.forms import fields
from principal.models import asignacion

class asignacionForm(forms.ModelForm):
    class Meta:
        model = asignacion
        fields = '__all__'