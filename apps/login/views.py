from django.shortcuts import render


# Create your views here.

def login(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)
