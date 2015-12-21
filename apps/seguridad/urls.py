# -*- coding: utf-8
from django.conf.urls import patterns, include, url
from .views import *
from .import views

urlpatterns = patterns('',
    url(r'^$',vista_inicio),
    url(r'^login/$',vista_login),
    url(r'^puertas/$',vista_puertas),
    url(r'^index/$',index_view,name='index'),
    url(r'^registros/$', registros, name='registros'),
    url(r'^usuarios/$', usuarios, name='usuarios'),
    url(r'^puertas/$', vista_puertas, name='puertas'),
    url(r'^usuarios/ingresarusuario/$', ingresarusuario, name='ingresarusuario'),
    url(r'^usuarios/modificarcontrasena/$', modificarcontrasena, name='modificarcontrasena'),
    )
