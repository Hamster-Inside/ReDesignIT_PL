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
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        new_slug = f'{slugify(self.name)}-{self.pk}'
        if self.slug != new_slug:
            self.slug = new_slug
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
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        new_slug = f'{slugify(self.title)}-{self.pk}'
        if self.slug != new_slug:
            self.slug = new_slug
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title
