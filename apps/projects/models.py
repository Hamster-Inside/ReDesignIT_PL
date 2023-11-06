from django.db import models


# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    project_name = models.CharField(max_length=100, default='Project Name')
    summary = models.TextField()
    slug = models.SlugField(default="", null=False)
    github_url = models.CharField(max_length=150, blank=True)
    youtube_url = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.project_name
