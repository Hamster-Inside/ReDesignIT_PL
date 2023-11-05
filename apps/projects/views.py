from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Project


# Create your views here.

def projects(request):
    my_projects = Project.objects.all()
    template = 'projects.html'
    context = {'my_projects': my_projects}
    return render(request, template, context)


def project_detail(request, pk):
    template = 'project-detail.html'
    try:
        picked_project = Project.objects.get(pk=pk)
        context = {'project': picked_project}
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, template, context)
