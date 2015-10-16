# -*- coding: utf-8 -*-
"""tryDjango18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^home/$', 'newsLetter.views.home', name='home'),
    url(r'^home/contact/$', 'newsLetter.views.contact', name='contact'),
    url(r'^home/protegida/$', 'newsLetter.views.protegida', name='protegida'),
    url(r'^home/about/$', 'tryDjango18.views.about', name='about'),

    url(r'^home/login/$', 'newsLetter.views.autenticado', name='login'),
    url(r'^home/registrar/$', 'newsLetter.views.registrar', name='registrar'),
    url(r'^home/sair/$', 'newsLetter.views.sair', name='sair'),


    url(r'^home/index/$', 'newsLetter.views.index', name='index'),
    url(r'^home/upload/$', 'newsLetter.views.Upload', name='upload'),
    url(r'^home/(?P<id>\d+)/$', 'newsLetter.views.detail', name='detail'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)