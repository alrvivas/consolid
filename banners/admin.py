from django.contrib import admin

from .models import Categoria,Banner

@admin.register(Categoria)
class tipo_empleadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre',)
	search_fields = ('nombre',)

@admin.register(Banner)
class empleadoAdmin(admin.ModelAdmin):
	list_display = ('id','activo','categoria','titulo')
	search_fields = ('categoria',)