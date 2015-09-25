# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import SignUp

class SignUpForm(forms.ModelForm):

	class Meta:

		model = SignUp

		fields = ['email', 'nomeCompleto', 'mensagem']

		help_text = {
			'email'			: "Esse e-mail é para entrarmos em contado",
			'nomeCompleto'	: "Edfsdfsdf gsdf  sdfs sfd sfsdf "
		}

		labels = {
			'email'			: ('e-mail'),
			'nomeCompleto'	: ('Nome Completo')
		}

		widgets = {
			'email'			: forms.TextInput(attrs={'placeholder': u'Digite o e-mail do usuário'}),
			'nomeCompleto'	: forms.TextInput(attrs={'placeholder': u'Digite o nome completo'}),
            'mensagem'		: forms.Textarea(attrs={'placeholder': u'Digite aqui a sua mensagem...'}),
        }


	def clean_email(self):
		email = self.cleaned_data.get('email')

		email_base, provider = email.split("@")
		domain, extension = provider.split('.')

		if not extension == "com":
			raise forms.ValidationError(u'Por favor insira um email validado .edi [ %s ]' % email)
		return email
# Login
class LoginForm(forms.Form):

	username = forms.CharField(label='Usuário de acesso', max_length=30,
								widget=forms.TextInput(attrs={'placeholder':'Usuário de acesso..'}))
	password = forms.CharField(label='Senha de acesso', max_length=30,
								widget = forms.PasswordInput(attrs={'placeholder':'Senha de acesso..'}),
								help_text = ("Enter the same password as above, for verification."))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		print User.objects.filter(username=username)

		if not User.objects.filter(username=username):
			raise forms.ValidationError(u'Esse usuário [ %s ] não existe' % username)
		return username

	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username, password=password):
			raise forms.ValidationError(u'Senha incorreta')
		return password

	def autenticar(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		return authenticate(username=username, password=password)

# Cadastro Usuario ao sistema
class RegistroForm(forms.Form):

	first_name = forms.CharField(label='Nome de Usuário', max_length=30)
	username = forms.CharField(label='Username', max_length=30)
	passwordr = forms.CharField(label='Senha do Usuário', max_length=30, widget = forms.PasswordInput)
	password = forms.CharField(label='Confirme a Senha', max_length=30, widget = forms.PasswordInput,
								help_text = ("Enter the same password as above, for verification."))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username):
			raise forms.ValidationError(u'Esse usuário [ %s ] já existe' % username)
		return username

	def clean_password(self):
		
		password = self.cleaned_data.get('password')
		passwordr = self.cleaned_data.get('passwordr')
		
		if not password == passwordr:
			raise forms.ValidationError(u'Senhas diferentes')

		return password

	def registrar(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		first_name = self.cleaned_data.get('first_name')
		user = User.objects.create_user(username, None, password)
		user.first_name = first_name
		user.save()
		return user