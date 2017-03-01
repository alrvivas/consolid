from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado

class Comunicado(models.Model):
	empleado = models.ForeignKey(Empleado)
	nombre =  models.CharField(max_length=140)
	vigente = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_vigencia = models.DateTimeField(blank=True,null=True)
	descripcion = models.TextField(blank=True,null=True)
	imagen = models.ImageField("Imagen Comunicado", upload_to="imagnes/comunicado", blank=True, null=True,default='images/default.png')	
	archivo = models.FileField("Archivo Comunicado", upload_to="archivos/comunicado", blank=True, null=True)

	def __str__(self):
		return self.nombre