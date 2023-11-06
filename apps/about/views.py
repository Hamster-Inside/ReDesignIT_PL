from django.shortcuts import render
from .models import About


# Create your views here.

def about(request):
    about_me = About.objects.first()
    template = 'about.html'
    context = {'about': about_me}
    return render(request, template, context)
