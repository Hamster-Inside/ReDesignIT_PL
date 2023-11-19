from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox


class LoginWithCaptchaForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        api_params={'hl': 'pl'},
        # attrs={'required_score': 0.85}
    ))


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        api_params={'hl': 'pl'},
        # attrs={'required_score': 0.85}
    ))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
