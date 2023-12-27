from collections import namedtuple
from os import getenv

from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django_registration.exceptions import ActivationError
from dotenv import load_dotenv
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import CustomRegistrationForm, LoginWithCaptchaForm
from django_registration.backends.activation.views import RegistrationView, ActivationView
from .email_sender import EmailSender
from django.utils.translation import gettext_lazy as _
import secrets
import string

from .models import CustomUser


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = LoginWithCaptchaForm
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        if self.request.POST.get('test_user_action') == 'register':
            captcha_form = self.authentication_form(request.POST)
            try:
                captcha_form.fields['captcha'].validate(request.POST['g-recaptcha-response'])
                user_id = str(CustomUser.objects.count() + 1)
                while True:
                    test_username = self.generate_random_username() + user_id
                    test_email = str(test_username + "@redesignit.pl").lower()
                    if not self.username_exists(test_username) and not self.email_exists(test_email):
                        break

                test_password = self.generate_random_password()
                test_user = CustomUser.objects.create_user(username=test_username, email=test_email,
                                                           password=test_password)

                test_user.is_active = True
                test_user.save()
                authenticated_user = authenticate(request, username=test_email, password=test_password)
                if authenticated_user:
                    login(request, authenticated_user)
                    next_url = self.request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    else:
                        return redirect("home")
            except ValidationError:
                pass

        return super().dispatch(request, *args, **kwargs)

    def generate_random_password(self):
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(12))
        return password

    def generate_random_username(self):
        characters = string.ascii_letters + string.digits
        username = "TestUser."
        username += ''.join(secrets.choice(characters) for _ in range(7))
        return str(username)

    def username_exists(self, test_username):
        return CustomUser.objects.filter(username=test_username).exists()

    # Check if an email exists
    def email_exists(self, test_email):
        return CustomUser.objects.filter(email=test_email).exists()


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
    template_name = "register.html"
    email_body_template = "django_registration/activation_email_body.html"

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
            try:
                connection.send_email(user.email, subject, message)
            except Exception as e:
                print(f"Error sending activation email: {e}")


class CustomActivationView(ActivationView):
    ALREADY_ACTIVATED_MESSAGE = _("Konto jest już aktywne. Zaloguj się.")
    BAD_USERNAME_MESSAGE = _("Błąd aktywacji konta. Skontaktuj się z administratorem.")
    EXPIRED_MESSAGE = _("Czas aktywacji minął. Zarejestruj się ponownie.")
    INVALID_KEY_MESSAGE = _("Klucz jest niepoprawny. Skontaktuj się z administratorem.")
    CONFIRMED_USER_DEACTIVATED = _("Konto zostało zawieszone. Skontaktuj się z administratorem")

    def activate(self, *args, **kwargs):
        try:
            username = self.validate_key(kwargs.get("activation_key"))
            user = self.get_user(username)

            if user.email_confirmed and not user.is_active:
                raise ActivationError(message=self.CONFIRMED_USER_DEACTIVATED, code="deactivated_user")

            user.email_confirmed = True
            user.is_active = True
            user.save()
            return user
        except ActivationError as exc:
            # TODO add my own context based on error
            raise ActivationError(exc.message, exc.code, exc.params)


class CustomLogoutView(LogoutView):
    next_page = "home"


# Added below function because of the Firefox problem auto-adding slash after URL and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
