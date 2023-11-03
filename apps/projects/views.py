from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project


# Create your views here.

def projects(request):
    my_projects = Project.objects.all()
    template = 'projects.html'
    context = {'my_projects': my_projects}
    return render(request, template, context)
