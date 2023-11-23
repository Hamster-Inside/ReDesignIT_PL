from django.urls import path, include
from . import views

from .forms import CustomRegistrationForm

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('login/', views.login_redirect, name='login_redirect'),
    path('register', views.CustomRegistrationView.as_view(), name='register'),
    path('register/', views.register_redirect, name='register_redirect'),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),
    path('', include('django_registration.backends.activation.urls')),
]
