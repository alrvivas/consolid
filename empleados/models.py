from django.db import models
from django.contrib.auth.models import User

class Tipo_Empleado(models.Model):
	nombre = models.CharField(max_length=140)

	def __str__(self):
		return self.nombre

class Empleado(models.Model):
	user = models.ForeignKey(User)
	tipo_empleado = models.ForeignKey(Tipo_Empleado)
	activo = models.BooleanField(default=True)
	telefono1 = models.CharField(max_length=20,null=True, blank=True)
	telefono2 = models.CharField(max_length=20,null=True, blank=True)
	celular = models.CharField(max_length=20,null=True, blank=True)
	email = models.CharField(max_length=80,null=True, blank=True)
	imagen = models.ImageField("Imagen Empleado", upload_to="imagenes/empleados", blank=True, null=True,default='imagenes/default.png')	

	def __str__(self):
		return str(self.user)