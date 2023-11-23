from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'my_projects'
    ordering = ['pk']


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'
    context_object_name = 'project'
    slug_url_kwarg = 'slug'
