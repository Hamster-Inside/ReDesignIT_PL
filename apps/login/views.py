from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, LoginWithCaptchaForm
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser
from django_registration.views import ActivationView
from django_registration.backends.activation.views import RegistrationView


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = LoginWithCaptchaForm
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        # messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = self.get_form()
        return context


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
    template_name = "register.html"

    # success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["register_form"] = self.get_form()
        print(context)
        return context


class CustomLogoutView(LogoutView):
    next_page = "home"


# Added below function because of the Firefox problem auto-adding slash after URL and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
