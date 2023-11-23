from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import CustomRegistrationForm, LoginWithCaptchaForm
from django_registration.backends.activation.views import RegistrationView


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = LoginWithCaptchaForm
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
    template_name = "register.html"


class CustomLogoutView(LogoutView):
    next_page = "home"


# Added below function because of the Firefox problem auto-adding slash after URL and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
