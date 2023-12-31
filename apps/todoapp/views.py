from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Task, TaskGroup
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import TaskGroupCreateForm, TaskGroupUpdateForm, TaskCreateForm, TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages


class TaskOwnershipMixin(LoginRequiredMixin):
    model = Task
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404("Task not found or you don't have permission.")
        return obj


class TaskGroupOwnershipMixin(LoginRequiredMixin):
    model = TaskGroup
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404("Task not found or you don't have permission.")
        return obj


class TaskGroupListView(LoginRequiredMixin, ListView):
    model = TaskGroup
    template_name = 'todoapp.html'
    context_object_name = 'taskgroup_list'
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return TaskGroup.objects.filter(author=self.request.user).order_by("pk")
        else:
            messages.warning(self.request, "You have to be logged in to see the tasks.")
            messages.add_message(self.request, messages.WARNING, "You have to be logged in to see the tasks.")
            return TaskGroup.objects.none()  # Return an empty queryset if not logged in


class TaskGroupCreateView(LoginRequiredMixin, CreateView):
    model = TaskGroup
    form_class = TaskGroupCreateForm
    template_name = 'todoapp-taskgroup-create.html'
    success_url = reverse_lazy('taskgroup_list')
    login_url = reverse_lazy(settings.LOGIN_URL)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskGroupTaskListView(TaskGroupOwnershipMixin, ListView):
    model = Task
    template_name = 'todoapp-taskgroup-detail.html'
    context_object_name = 'taskgroup'
    login_url = reverse_lazy(settings.LOGIN_URL)
    taskgroup = None

    def get(self, request, *args, **kwargs):
        self.taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(group=self.taskgroup).order_by("pk")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroup'] = self.taskgroup
        context['tasks'] = self.get_queryset()
        return context


class TaskGroupUpdateView(TaskGroupOwnershipMixin, UpdateView):
    model = TaskGroup
    form_class = TaskGroupUpdateForm
    template_name = 'todoapp-taskgroup-create.html'
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_object(self, queryset=None):
        # Get the TaskGroup object based on the taskgroup_slug parameter
        taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)
        return taskgroup

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy('taskgroup_detail', kwargs={'taskgroup_slug': self.object.slug})
        return success_url


class TaskGroupDeleteView(TaskGroupOwnershipMixin, DeleteView):
    model = TaskGroup
    template_name = 'todoapp-taskgroup-delete.html'
    context_object_name = 'taskgroup'
    success_url = reverse_lazy('taskgroup_list')
    login_url = reverse_lazy(settings.LOGIN_URL)
    object = None

    def get_object(self, queryset=None):
        # Get the TaskGroup object based on the taskgroup_slug parameter
        taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)
        return taskgroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroup'] = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'],
                                                 author=self.request.user)
        return context


class TaskDetailView(TaskOwnershipMixin, DetailView):
    model = Task
    template_name = 'todoapp-task-detail.html'
    context_object_name = 'task'
    login_url = reverse_lazy(settings.LOGIN_URL)
    object = None

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, slug=self.kwargs['task_slug'], author=self.request.user)
        self.object = task
        print(self.object)
        context = super().get_context_data(object=task)
        context['task'] = task
        context['taskgroup'] = task.group
        return self.render_to_response(context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'todoapp-task-create.html'
    success_url = reverse_lazy('taskgroup_detail')
    login_url = reverse_lazy(settings.LOGIN_URL)
    object = None

    def get(self, request, *args, **kwargs):
        taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)
        self.object = taskgroup
        context = self.get_context_data(object=taskgroup)
        return self.render_to_response(context)

    def form_valid(self, form):
        taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)
        form.instance.group = taskgroup
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        success_url = reverse_lazy('taskgroup_detail', kwargs={'taskgroup_slug': self.kwargs['taskgroup_slug']})
        return success_url


class TaskUpdateView(TaskOwnershipMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'todoapp-task-update.html'
    login_url = reverse_lazy(settings.LOGIN_URL)

    def get_object(self, queryset=None):
        # Get the TaskGroup object based on the taskgroup_slug parameter
        taskgroup = get_object_or_404(TaskGroup, slug=self.kwargs['taskgroup_slug'], author=self.request.user)

        # Get the Task object based on both taskgroup and task slugs
        task = get_object_or_404(Task, group=taskgroup, slug=self.kwargs['task_slug'], author=self.request.user)

        return task

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('taskgroup_detail', kwargs={'taskgroup_slug': self.kwargs['taskgroup_slug']})


class TaskDeleteView(TaskOwnershipMixin, DeleteView):
    model = Task
    template_name = 'todoapp-task-delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('taskgroup_detail')
    login_url = reverse_lazy(settings.LOGIN_URL)
    referer_url = None

    def get(self, request, *args, **kwargs):
        self.referer_url = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        task = get_object_or_404(Task, slug=self.kwargs['task_slug'], author=self.request.user)
        return task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, slug=self.kwargs['task_slug'],
                                            author=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('taskgroup_detail', kwargs={'taskgroup_slug': self.kwargs['taskgroup_slug']})
