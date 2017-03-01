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

from .models import Comunicado

@login_required(login_url='/login/')
def comunicados(request):
    page_title = "Comunicados Lineas Areas"
    user = request.user
    comunicados = Comunicado.objects.filter(vigente=True,fecha_vigencia__gte=datetime.datetime.today())
    template ="comunicados.html" 
    return render(request,template, locals())