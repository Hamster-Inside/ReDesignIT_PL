from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .data_log import log_to_file
from .models import ProgrammingLanguage, Framework, WebProfile, MyApp, Statistic
from ipware import get_client_ip
from .loc_data import get_user_location_data


class HomeView(TemplateView):
    template_name = 'index.html'
    client_ip = None
    user_data = None

    def dispatch(self, request, *args, **kwargs):
        self.client_ip, _ = get_client_ip(request)
        user_agent = request.user_agent
        log_to_file(self.client_ip, user_agent)
        if self.client_ip is not None:
            self.user_data = Statistic.objects.filter(ip_address=self.client_ip).first()
            if not self.user_data:
                self.user_data = Statistic.objects.create(ip_address=self.client_ip)
                user_location = get_user_location_data(self.client_ip)
                self.user_data.continent = user_location['continent_name']
                self.user_data.country = user_location['country_name']
                self.user_data.city = user_location['city']
            else:
                self.user_data.visit_count += 1
            self.user_data.save()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programming_languages'] = ProgrammingLanguage.objects.all()
        context['frameworks'] = Framework.objects.all()
        context['social_profiles'] = WebProfile.objects.all()
        context['apps'] = MyApp.objects.all()

        return context


class StatisticView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'statistic.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_location_data'] = Statistic.objects.all()
        print(context)
        return context
