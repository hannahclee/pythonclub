from django.shortcuts import render, get_object_or_404
from .models import Resource
from .models import Meeting

# Create your views here.

def index(request) :
    return render(request, 'pythonclubapp/index.html')

def resources (request):
    resource_list=Resource.objects.all()
    return render (request, 'pythonclubapp/resources.html' , {'resource_list': resource_list})

def meetings (request):
    meeting_list=Meeting.objects.all()
    return render (request, 'pythonclubapp/meetings.html' , {'meeting_list': meeting_list})

def meetingdetail (request, id): 
    detail=get_object_or_404(Meeting, pk=id)
    context = {'detail': detail}
    return render (request, 'pythonclubapp/details.html' , context=context)