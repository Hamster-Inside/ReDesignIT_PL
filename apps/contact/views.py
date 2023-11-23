from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contact


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_me'] = Contact.objects.first()
        return context
