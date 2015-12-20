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



    
