import logging
from django.views.generic import TemplateView

from .models import ProgrammingLanguage, Framework, WebProfile, MyApp
from ipware import get_client_ip

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programming_languages'] = ProgrammingLanguage.objects.all()
        context['frameworks'] = Framework.objects.all()
        context['social_profiles'] = WebProfile.objects.all()
        context['apps'] = MyApp.objects.all()

        client_ip, is_routable = get_client_ip(self.request)
        if client_ip is None:
            print('ip is none')  # Unable to get the client's IP address
        else:
            print(f'Client IP: {client_ip}')  # We got the client's IP address
            if is_routable:
                print('Clients IP is routable')  # The client's IP address is publicly routable on the Internet
            else:
                print('IP is private')  # The client's IP address is private

        user_agent = self.request.user_agent

        logger.info(f' | Browser: {user_agent.browser.family} | '
                    f'Version: {user_agent.browser.version_string} | '
                    f'Device: {user_agent.device} | '
                    f'OS: {user_agent.os.family} '
                    f'{user_agent.os.version_string}')

        return context
