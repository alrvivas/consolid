from django.contrib import admin

from .models import Comunicado

@admin.register(Comunicado)
class tipo_empleadoAdmin(admin.ModelAdmin):
	list_display = ('id','vigente','nombre','fecha_creacion','fecha_vigencia')
	search_fields = ('nombre',)