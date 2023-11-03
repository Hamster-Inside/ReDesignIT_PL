from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProgrammingLanguage, Framework, WebProfile


# Create your views here.

def home(request):
    programming_languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    social_profiles = WebProfile.objects.all()
    template = 'index.html'
    context = {'programming_languages': programming_languages, 'frameworks': frameworks,
               'social_profiles': social_profiles}
    return render(request, template, context)
