from collections import OrderedDict
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _
from django_registration.forms import RegistrationForm

from apps.login.models import CustomUser


class LoginWithCaptchaForm(AuthenticationForm):
    fields = ['email', 'password', 'captcha']
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True, "autocomplete": "email"}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        api_params={'hl': 'pl'},
        # attrs={'required_score': 0.85}
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        new_fields = OrderedDict()
        new_fields['email'] = self.fields['email']
        new_fields['password'] = self.fields['password']
        new_fields['captcha'] = self.fields['captcha']
        self.fields = new_fields

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class CustomRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(api_params={'hl': 'pl'}, ))

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        if 'captcha' not in self.fields:
            self.fields['captcha'] = self.captcha
        for name, field in self.fields.items():
            if not name == 'captcha':
                field.widget.attrs.update({'class': 'form-control'})
