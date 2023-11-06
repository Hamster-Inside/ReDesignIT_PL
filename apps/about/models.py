from django.db import models


# Create your models here.

class About(models.Model):
    about_text = models.TextField()

    def __str__(self):
        return 'About Me'
