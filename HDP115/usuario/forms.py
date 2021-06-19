from django import forms
from django.forms import fields
from principal.models import persona
from principal.models import usuario
from principal.models import administrador

#Formulario para Crear Personas
class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = ('__all__')
#Formulario para crear Usuarios
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('__all__')
#Formulario para crear Administradores
class AdminForm(forms.ModelForm):
    class Meta:
        model = administrador
        fields = ('__all__')