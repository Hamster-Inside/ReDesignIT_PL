from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskGroupListView.as_view(), name='taskgroup_list'),
    path('tasks/create', views.TaskGroupCreateView.as_view(), name='taskgroup_create'),
    path('tasks/<slug:taskgroup_slug>/', views.TaskGroupTaskListView.as_view(), name='taskgroup_detail'),
    path('tasks/<slug:taskgroup_slug>/update', views.TaskGroupUpdateView.as_view(), name='taskgroup_update'),
    path('tasks/<slug:taskgroup_slug>/delete', views.TaskGroupDeleteView.as_view(), name='taskgroup_delete'),
    path('tasks/<slug:taskgroup_slug>/create', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<slug:taskgroup_slug>/<slug:task_slug>/update', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<slug:taskgroup_slug>/<slug:task_slug>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<slug:taskgroup_slug>/<slug:task_slug>/', views.TaskDetailView.as_view(), name='task_detail'),
]