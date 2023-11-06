from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact


# Create your views here.

def contact(request):
    contact_me = Contact.objects.first()
    template = 'contact.html'
    context = {'contact_me': contact_me}
    return render(request, template, context)
