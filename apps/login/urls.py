from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('login/', views.login_redirect, name='login_redirect'),
    path('register', views.CustomRegistrationView.as_view(), name='register'),
    path('register/', views.register_redirect, name='register_redirect'),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),
    path("activate/complete/", TemplateView.as_view(template_name="django_registration/activation_complete.html"),
         name="django_registration_activation_complete"),
    path("activate/<str:activation_key>/", views.CustomActivationView.as_view(), name="django_registration_activate"),
    path("register/complete/", TemplateView.as_view(template_name="django_registration/registration_complete.html"),
         name="django_registration_complete"),
    path("register/closed/", TemplateView.as_view(template_name="django_registration/registration_closed.html"),
         name="django_registration_disallowed"),
]
