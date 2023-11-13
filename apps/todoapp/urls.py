from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<slug:slug>', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<slug:slug>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<slug:slug>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]