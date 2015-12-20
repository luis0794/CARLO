from django.shortcuts import render, RequestContext, render_to_response
from django.http import request, HttpResponse, HttpResponseRedirect, Http404


import time

# Create your views here.

def vista_inicio(request):
    return render_to_response('inicio.html',context=RequestContext(request))

def vista_login(request):
	return render_to_response('login.html',context=RequestContext(request))


def vista_puertas(request):
	return render_to_response('puerta.html',context=RequestContext(request))


def index_view(request):
    return render_to_response('index.html',context=RequestContext(request))

def registros(request):
    return render_to_response('registros.html',context=RequestContext(request))

def usuarios(request):
    return render_to_response('usuarios.html',context=RequestContext(request))

def ingresarusuario(request):
    return render_to_response('ingresarusuario.html',context=RequestContext(request))

def modificarcontrasena(request):
    return render_to_response('modificarcontrasena.html',context=RequestContext
    
