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

from .models import Empleado
from banners.models import Categoria,Banner

@login_required(login_url='/login/')
def index(request):
    page_title = "Consolidadora"
    user = request.user
    categoria = Categoria.objects.filter(id=1)
    banners = Banner.objects.filter(categoria=categoria)
    template ="index.html" 
    return render(request,template, locals())