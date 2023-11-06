from django.db import models


# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    project_name = models.CharField(max_length=100, default='Project Name')
    summary = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.project_name
