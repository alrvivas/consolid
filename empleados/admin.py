from django.contrib import admin

from .models import Empleado,Tipo_Empleado

@admin.register(Tipo_Empleado)
class tipo_empleadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre',)
	search_fields = ('nombre',)

@admin.register(Empleado)
class empleadoAdmin(admin.ModelAdmin):
	list_display = ('id','activo','tipo_empleado','celular')
	search_fields = ('tipo_empleado','celular')