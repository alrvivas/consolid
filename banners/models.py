from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=140)

	def __str__(self):
		return self.nombre

class Banner(models.Model):
	categoria = models.ForeignKey(Categoria)
	activo = models.BooleanField(default=True)
	orden = models.IntegerField(null=True, blank=True)
	titulo = models.CharField(max_length=64,null=True, blank=True)
	descripcion = models.CharField(max_length=140,null=True, blank=True)	
	fecha_publicacion = models.DateField(null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField("Imagen Banner", upload_to="imagenes/banners", blank=True, null=True)	

	def __unicode__(self):
		return self.user