from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(
		help_text="A unique title for this thing")
	nomeCompleto = models.CharField(max_length=140, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	atualizacao = models.DateTimeField(auto_now_add=False, auto_now=True)
	mensagem = models.TextField(max_length=500, blank=True, null=True)
	photo = models.FileField(upload_to="projectimg/")

	def __unicode__(self):
		return self.email

class UserProfile (models.Model):
	Usuario = models.OneToOneField(User, related_name='user_profile')

	Aniversario = models.DateField(u'Aniversario', null = True)

	def __unicode__ (self):
		return self.user.username

#
#class Login(models.Model):
#	username = models.CharField(max_length=30)
#	password = models.CharField(max_length=30, widget=forms.passwordInput)
