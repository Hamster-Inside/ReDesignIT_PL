from django.db import models


# Create your models here.

class About(models.Model):
    about_text = models.TextField()

    def __str__(self):
        return 'About Me'


class AboutImages(models.Model):
    title = models.CharField(max_length=100, default='Title', null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)

    def __str__(self):
        return self.title
