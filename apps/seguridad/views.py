from django.shortcuts import render, RequestContext, render_to_response, redirect
from django.http import request, HttpResponse, HttpResponseRedirect, Http404
from .forms import RegistroUserForm

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from .forms import RegistroUserForm
from .models import UserProfile


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
    return render_to_response('usuarios.html',context=RequestContext(request))

def ingresarusuario(request):
	if request.method == 'POST':
		form = RegistroUserForm(request.POST, request.FILES)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			password = cleaned_data.get('password')
			photo = cleaned_data.get('photo')
			user_model = User.objects.create_user(username=username, password=password)
			user_model.save()
			user_profile = UserProfile()
			user_profile.user = user_model
			user_profile.photo = photo
			user_profile.save()
			return redirect(reverse('usuarios.html', kwargs={'username': username}))
		else:
			form = RegistroUserForm()
		context = {'form': form}
		return render(request, 'usuarios.html', context)


def gracias_view(request, username):
    return render(request, 'usuarios', {'username': username})

def modificarcontrasena(request):
    return render_to_response('modificarcontrasena.html',context=RequestContext(request))  
