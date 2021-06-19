from django.contrib import admin

from .models import persona
from .models import usuario
from .models import administrador
from .models import zona 
from .models import asignacion
from .models import paqueteAlimentario
from .models import entregaPaquete
# Register your models here.

admin.site.register(persona)
admin.site.register(usuario)
admin.site.register(administrador)
admin.site.register(zona)
admin.site.register(asignacion)
admin.site.register(paqueteAlimentario)
admin.site.register(entregaPaquete)


