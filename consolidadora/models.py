from django.db import models
from django.contrib.auth.models import User

class Consolidadora(models.Model):
	user = models.ForeignKey(User)
	activa = models.BooleanField(default=True)
	telefono1 = models.CharField(max_length=20,null=True, blank=True)
	telefono2 = models.CharField(max_length=20,null=True, blank=True)
	celular = models.CharField(max_length=20,null=True, blank=True)
	email = models.CharField(max_length=80,null=True, blank=True)
	imagen = models.ImageField("Imagen Consolidadora", upload_to="imagnes/consolidadora", blank=True, null=True,default='images/default.png')	

	def __str__(self):
		return self.nombre