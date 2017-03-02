from django.conf.urls import url
from comisiones.views import tabla_comisiones,tabla_comision

urlpatterns = [
    url(r'^$', tabla_comisiones, name='tabla-comisiones'),
    url(r'^(?P<tabla_slug>[-\w]+)/$',tabla_comision, name='tabla-comision'),
]