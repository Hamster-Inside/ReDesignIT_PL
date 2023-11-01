from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project


# Create your views here.

def projects(request):
    my_projects = Project.objects
    template = loader.get_template('projects.html', {'Projects:': my_projects})
    return HttpResponse(template.render())
