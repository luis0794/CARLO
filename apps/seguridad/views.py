from django.shortcuts import render, RequestContext, render_to_response
from django.http import request, HttpResponse, HttpResponseRedirect, Http404

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext

from .forms import SignUpForm

from .models import *


import time

# Create your views here.

def vista_inicio(request):
    return render_to_response('inicio.html',context=RequestContext(request))

def vista_login(request):
	return render_to_response('login.html',context=RequestContext(request))


def vista_puertas(request):
	return render_to_response('puerta.html',context=RequestContext(request))


def index_view(request):
    return render_to_response('inicio.html',context=RequestContext(request))

def registros(request):
    return render_to_response('registros.html',context=RequestContext(request))

def usuarios(request):
	usu=UserProfile.objects.all()
	return render_to_response('usuarios.html',{'usu':usu},context_instance=RequestContext(request))
	
	
def ingresarusuario(request):
	if request.method == 'POST': 
		form = SignUpForm(request.POST)  # A form bound to the POST data
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			user = User.objects.create_user(username, password)
			user.first_name = first_name
			user.last_name = last_name

			user.save()

			return HttpResponseRedirect(reverse('usuarios'))
	else:
		form = SignUpForm()

	data = {
		'form': form,
	}
	return render_to_response('ingresarusuario.html', data, context_instance=RequestContext(request))


def modificarcontrasena(request):
    return render_to_response('modificarcontrasena.html',context=RequestContext(request))  
