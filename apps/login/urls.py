from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('login/', views.login_redirect, name='login_redirect'),
    path('register', views.register_request, name='register'),
    path('register/', views.register_redirect, name='register_redirect'),
    path("logout", views.logout_request, name="logout"),
]
