from django.shortcuts import render
from django.http import HttpResponse
from .models import metrics,metadata
# Create your views here.

def index(request):
	return HttpResponse("Hello World. At dev index.")

def md(request):
	obj = metadata(1,2,3,4,5)
	return_value = obj.response()
	return HttpResponse(return_value)

def met(request):
	obj = metrics([5,6,7,8,9])
	value = obj.attributes([1,2,3])
	return HttpResponse(value)