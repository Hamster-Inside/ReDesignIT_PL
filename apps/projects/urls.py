from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>', views.project_detail, name='project-detail'),
]
