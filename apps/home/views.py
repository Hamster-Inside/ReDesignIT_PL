import logging
from django.views.generic import TemplateView

from .models import ProgrammingLanguage, Framework, WebProfile

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programming_languages'] = ProgrammingLanguage.objects.all()
        context['frameworks'] = Framework.objects.all()
        context['social_profiles'] = WebProfile.objects.all()

        user_agent = self.request.user_agent
        logger.info(f' | Browser: {user_agent.browser.family} | '
                    f'Version: {user_agent.browser.version_string} | '
                    f'Device: {user_agent.device} | '
                    f'OS: {user_agent.os.family} '
                    f'{user_agent.os.version_string}')

        return context
