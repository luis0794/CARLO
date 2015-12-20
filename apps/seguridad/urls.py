# -*- coding: utf-8
from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    url(r'^$',vista_inicio),
    url(r'^login/$',vista_login),
    url(r'^puertas/$',vista_puertas),

)
