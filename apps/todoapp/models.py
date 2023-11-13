from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Task(models.Model):
    todo_user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
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
