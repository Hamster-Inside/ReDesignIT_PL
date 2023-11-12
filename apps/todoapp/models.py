from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class TodoList(models.Model):
    todo_user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    todo_list_name = models.CharField(max_length=100, default='New Todo List')


class Task(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='New Title')
    description = models.TextField(default='NULL Description')
    is_done = models.BooleanField(default=False)
