from django.shortcuts import render
from django.http import Http404
from .models import TodoList, Task


def todo_app(request):
    todo_lists = TodoList.objects.all()
    template = 'todoapp.html'
    context = {'todo_lists': todo_lists}
    return render(request, template, context)


def todo_app_list(request, pk):
    tasks = Task.objects.all()
    template = 'todoapp-tasks.html'
    try:
        tasks = Task.objects.get(pk=pk)
        context = {'tasks': tasks}
    except Task.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, template, context)