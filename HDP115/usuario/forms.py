from django import forms
from principal.models import persona
from principal.models import usuario
from principal.models import administrador

class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = ('__all__')
