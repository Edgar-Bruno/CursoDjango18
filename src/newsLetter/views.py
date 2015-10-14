# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory


from .forms import SignUpForm, LoginForm, RegistroForm, SugnUpIMGForm
from .models import SignUp, SugnUpIMG


def home(request):

	if request.method == 'POST':

		formOBJ = SignUpForm(request.POST, request.FILES)

		print request.FILES

		if formOBJ.is_valid():
			instance = formOBJ.save(commit=False)

			instance.save()

			for key in request.FILES.getlist("photos"):
				SugnUpIMG.objects.create(signup_id=instance.id, photos=key)

			contexto = {
				"tituloForm"	: "Obrigado!",
				"vFlag"			: 1,
				"img"			: instance
			}

	else:

		titulo = "Escreva aqui a sua mensagem na home"

		contexto = {
		"tituloForm": titulo,
		"Formulario": SignUpForm(),
		"UploadIn"	: SugnUpIMGForm()
		}	

	return render(request, 'home.html', contexto)

def index(request):
	return render(request, 'upload.html', {})


def Upload(request):

	print '-------->'
	print (request.FILES.getlist("files_EDi"))
	print '-------->'
	for count, x in enumerate(request.FILES.getlist("files_EDi")):
		print 'sanjiro--- > %s' % x
		def process(f):
			with open('' + str(f), 'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
		process(x)
	
	return HttpResponse('Upados')


@login_required
def contact(request):

	titulo = "Escreva aqui a sua mensagem"

	formOBJCont = SignUpForm(request.POST or None)

	contexto = {
			"tituloForm"	: titulo,
			"FormularioC"	: formOBJCont
	}
	

	if formOBJCont.is_valid():
		instance = formOBJCont.save(commit=False)
		instance.save()


		contexto = {
			"tituloForm"	: "Obrigado!",
			"vFlag"			: 1
		}

	contexto = {
			"tituloForm"	: titulo,
			"FormularioC"	: formOBJCont
	}


	for instace in SignUp.objects.all():
		print "ID [ %d ] - %s" % (instace.id, instace.nomeCompleto)

	return render(request, 'contact.html', contexto)

def autenticado(request):

	loginOBJ = LoginForm(request.POST or None)


	if loginOBJ.is_valid():
		userX = loginOBJ.autenticar()
		login(request, userX)

		contexto = {
			"tituloForm": "Autenticado com sucesso.", #% userX.first_name,
			"method"	: "GET",
			"action"	: "/home/",
			"botao" 	: "Voltar",
			"Options"	: "btn-success"
		}

	else:

		if request.user.is_authenticated():
			# Do something for authenticated users.
			contexto = {
				"tituloForm": "Autenticado com usuario %s" % request.user.first_name,
				"action"	: "/home/",
				"botao"		: "ok",
				"Options"	: "btn-info"

			}
		else:
			# Do something for anonymous users.
			contexto = {
				"tituloForm": "Autentique-se",
				"loginFrom"	: loginOBJ,
				"method"	: "POST",
				"action"	: ".",
				"botao"		: "Logar",
				"Options"	: "btn-primary"
			}
	
	return render(request, 'login.html', contexto)

def sair(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

@login_required
def protegida(request):
	# TEste do decorator

	return HttpResponse('Só com logi aceito')

def registrar(request):

	registrarOBJ = RegistroForm(request.POST or None)

	if request.user.is_authenticated():

		contexto = {
			"tituloForm": "Autenticado com usuario %s" % request.user.first_name,
			"action"	: "/home/",
			"botao"		: "ok",
			"Options"	: "btn-info"
		}

	else:

		contexto = {
				"tituloForm": "Criar Usuário",
				"Registrar"	: registrarOBJ,
				"method"	: "POST",
				"action"	: ".",
				"botao"		: "Criar",
				"Options"	: "btn-primary"
		}

		# print User.objects.filter(username=username)

		if registrarOBJ.is_valid():

			instance = registrarOBJ.registrar()
				
			contexto = {
				"tituloForm": "Usuário Criado",
				"action"	: "/home/",
				"botao"		: "ok",
				"Options"	: "btn-info"
			}

	#print registrarOBJ.cleaned_data['passwordr']
	return render(request, 'registrar.html', contexto)