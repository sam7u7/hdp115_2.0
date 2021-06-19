from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import ModelSignal

# Create your models here.

class persona(models.Model):
    idpersona  = models.AutoField(primary_key=True)
    dui = models.CharField(max_length=9,unique=True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    numeroTelefono = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=254)
    rol = models.IntegerField(default=1, validators=[MaxValueValidator(2),MinValueValidator(1)])

    def __str__(self):
        return str(self.nombre) 

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(persona, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return str(self.idUsuario)

class administrador(models.Model):
    idAdministrador = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(persona, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return str(self.idAdministrador)


class zona(models.Model):
    codigoZona = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return str(self.codigoZona)

class asignacion(models.Model):
    idcomprobante = models.AutoField(primary_key=True)
    idAdmistrador = models.ForeignKey(administrador, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    codigoZona = models.ForeignKey(zona, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fechaDeAsignacion = models.DateField()

    def __str__(self):
        return str(self.idcomprobante)
    


class paqueteAlimentario(models.Model):
    codigo = models.AutoField(primary_key=True)
    idAdministrador = models.ForeignKey(administrador, on_delete=models.CASCADE)
    fechaDeExpedicion = models.DateField()
    fechaDeCaducidad = models.DateField()

    def __str__(self):
        return str(self.codigo) 

class entregaPaquete(models.Model):
    idEntrega = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=50)
    dui = models.CharField(max_length=9,unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default = False)