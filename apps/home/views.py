import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProgrammingLanguage, Framework, WebProfile

# Create your views here.
logger = logging.getLogger(__name__)


def home(request):
    logger.info(f' | Browser: {request.user_agent.browser.family} | '
                f'Version: {request.user_agent.browser.version_string} | '
                f'Device: {request.user_agent.device} | '
                f'OS: {request.user_agent.os.family} '
                f'{request.user_agent.os.version_string}')
    programming_languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    social_profiles = WebProfile.objects.all()
    template = 'index.html'
    context = {'programming_languages': programming_languages, 'frameworks': frameworks,
               'social_profiles': social_profiles}
    return render(request, template, context)
