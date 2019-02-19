from django.shortcuts import render
from .models import Resource

# Create your views here.

def index(request) :
    return render(request, 'pythonclubapp/index.html')

def resources (request):
    resource_list=Resource.objects.all()
    return render (request, 'pythonclubapp/resources.html' , {'resource_list': resource_list})