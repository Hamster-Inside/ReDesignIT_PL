from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginWithCaptchaForm
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser
from django_registration.views import RegistrationView, ActivationView


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
        print(context)
        return context


class TwoPhaseRegisterView(RegistrationView):
    form_class = NewUserForm
    success_url = None
    template_name = "register.html"

    def register(self, form):
        pass


class TwoPhaseActivationView(ActivationView):
    success_url = reverse_lazy("home")
    template_name = "django_registration/activation_failed.html"

    def activate(self, *args, **kwargs):
        pass


# class CustomRegisterView(View):
#     template_name = "register.html"
#
#     def get(self, request, *args, **kwargs):
#         form = NewUserForm()
#         return render(request, self.template_name, {"register_form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.save()
#
#             return redirect("home")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#         return render(request, self.template_name, {"register_form": form})


class CustomLogoutView(LogoutView):
    next_page = "home"


# Added below function because of the Firefox problem auto-adding slash after URL and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
