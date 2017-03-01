from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from comunicados.views import comunicados

urlpatterns = [
    url(r'^$', comunicados, name='comunicados'),
]