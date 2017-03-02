from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.models import modelformset_factory
from django.db.models import Q 
import datetime

from .models import Tabla_Comisiones,Comisiones

@login_required(login_url='/login/')
def tabla_comisiones(request):
    page_title = "Comisiones"
    user = request.user
    tabla_comisiones = Tabla_Comisiones.objects.filter(vigente=True)
    comisiones = Comisiones.objects.filter(tabla_comisiones=tabla_comisiones,fecha_vigencia__gte=datetime.datetime.today())
    template ="comisiones.html" 
    return render(request,template, locals())

@login_required(login_url='/login/')
def tabla_comision(request,tabla_slug):
    page_title = "Comisiones"
    user = request.user
    tabla_comision = get_object_or_404(Tabla_Comisiones, slug=tabla_slug)
    comisiones = Comisiones.objects.filter(tabla_comisiones=tabla_comision,fecha_vigencia__gte=datetime.datetime.today())
    template ="tabla-comision.html" 
    return render(request,template, locals())