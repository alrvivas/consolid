from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado

class Tabla_Comisiones(models.Model):
	empleado = models.ForeignKey(Empleado)
	nombre = models.CharField(max_length=140)
	slug = models.SlugField(unique=True,null=True, blank=True)
	vigente = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

	@models.permalink
	def get_tabla(self):
		return ('tabla-comision', (), { 'tabla_slug': self.slug })

class Comisiones(models.Model):
	empleado = models.ForeignKey(Empleado)
	tabla_comisiones = models.ForeignKey(Tabla_Comisiones)
	vigente = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_vigencia = models.DateTimeField(blank=True,null=True)
	comision = models.CharField(max_length=10)
	venta_minima = models.DecimalField(max_digits=12,decimal_places=2)
	venta_maxima = models.DecimalField(max_digits=12,decimal_places=2)
	descripcion = models.TextField(blank=True,null=True)

	def __str__(self):
		return str(self.tabla_comisiones)

