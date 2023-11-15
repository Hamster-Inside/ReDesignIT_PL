from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class TaskGroup(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Default Name")
    slug = models.SlugField(unique=True, default="", null=False)
    is_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(TaskGroup, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='New Title')
    description = models.TextField(default='NULL Description')
    is_done = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default="", null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
