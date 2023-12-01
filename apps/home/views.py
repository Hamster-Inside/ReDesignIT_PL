from django.views.generic import TemplateView
from .data_log import log_to_file
from .models import ProgrammingLanguage, Framework, WebProfile, MyApp


class HomeView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        log_to_file(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programming_languages'] = ProgrammingLanguage.objects.all()
        context['frameworks'] = Framework.objects.all()
        context['social_profiles'] = WebProfile.objects.all()
        context['apps'] = MyApp.objects.all()

        return context
