from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskGroupListView.as_view(), name='taskgroup_list'),
    path('tasks/<slug:task_group_slug>', views.TaskListView.as_view(), name='task_list'),
    path('tasks/<slug:task_group_slug>/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<slug:task_group_slug>/<slug:task_slug>', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<slug:task_group_slug>/<slug:task_slug>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<slug:task_group_slug>/<slug:task_slug>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]