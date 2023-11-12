from django.urls import path
from . import views

urlpatterns = [
    path('todoapp', views.todo_app, name='todoapp'),
    path('todoapp/<int:pk>', views.todo_app_list, name='todoapp-tasks'),
]