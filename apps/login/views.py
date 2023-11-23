from collections import namedtuple
from os import getenv
from dotenv import load_dotenv
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import CustomRegistrationForm, LoginWithCaptchaForm
from django_registration.backends.activation.views import RegistrationView
from .email_sender import EmailSender


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

    def send_activation_email(self, user):
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context["user"] = user
        subject = render_to_string(
            template_name=self.email_subject_template,
            context=context,
            request=self.request,
        )
        # Force subject to a single line to avoid header-injection
        # issues.
        subject = "".join(subject.splitlines())
        message = render_to_string(
            template_name=self.email_body_template,
            context=context,
            request=self.request,
        )
        load_dotenv()
        Credentials = namedtuple('Credentials', 'username, password')
        credentials = Credentials(getenv('EMAIL'), getenv('GMAIL_PASSWORD_FOR_APPLICATION'))
        ssl_enabled = getenv('SSL_ENABLED')
        port = getenv('PORT')
        smtp_server = getenv('SMTP_SERVER')
        with EmailSender(port, smtp_server, credentials, ssl_enabled) as connection:
            connection.send_mail(user.email, subject, message)


class CustomLogoutView(LogoutView):
    next_page = "home"


# Added below function because of the Firefox problem auto-adding slash after URL and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
