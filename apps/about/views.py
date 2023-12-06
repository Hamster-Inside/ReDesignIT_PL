from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About, AboutImage


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['images'] = AboutImage.objects.all()
        return context
