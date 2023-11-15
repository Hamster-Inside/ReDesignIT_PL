from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class TaskGroup(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default="", null=False)
    is_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default="", null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
