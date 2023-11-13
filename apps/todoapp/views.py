from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


class TaskOwnershipMixin(LoginRequiredMixin):
    model = Task
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.todo_user != self.request.user:
            raise Http404("Task not found or you don't have permission.")
        return obj


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todoapp.html'
    context_object_name = 'tasks'
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_queryset(self):
        return Task.objects.filter(todo_user=self.request.user).order_by("pk")


class TaskDetailView(TaskOwnershipMixin, DetailView):
    model = Task
    template_name = 'todoapp-single-task.html'
    context_object_name = 'task'
    login_url = reverse_lazy(settings.LOGIN_URL)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoapp-task-create.html'
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy(settings.LOGIN_URL)

    def form_valid(self, form):
        form.instance.todo_user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskOwnershipMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoapp-task-create.html'
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy(settings.LOGIN_URL)

    def form_valid(self, form):
        form.instance.todo_user = self.request.user
        return super().form_valid(form)


class TaskDeleteView(TaskOwnershipMixin, DeleteView):
    model = Task
    template_name = 'todoapp-confirm-task-delete.html'
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy(settings.LOGIN_URL)

    def delete(self, request, *args, **kwargs):
        self.object = get_object_or_404(Task, slug=kwargs['slug'], todo_user=self.request.user)
        return super().delete(request, *args, **kwargs)
