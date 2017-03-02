from django.contrib import admin
from .models import Tabla_Comisiones,Comisiones

@admin.register(Tabla_Comisiones)
class tabla_comisionesAdmin(admin.ModelAdmin):
	list_display = ('id','vigente','nombre','fecha_creacion')
	search_fields = ('nombre',)

	prepopulated_fields = {'slug' : ('nombre',)} 

@admin.register(Comisiones)
class comisionesAdmin(admin.ModelAdmin):
	list_display = ('id','vigente','tabla_comisiones','venta_minima','venta_maxima','fecha_creacion','fecha_vigencia')
	search_fields = ('tabla_comisiones',)