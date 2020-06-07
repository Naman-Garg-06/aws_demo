from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^metadata/$', views.md, name='md'),
	url(r'^metrics/$', views.met, name='met')
]