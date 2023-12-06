from django.db import models
from image_cropping import ImageRatioField


# Create your models here.

class About(models.Model):
    about_text = models.TextField()

    def __str__(self):
        return 'About Me'


class AboutImage(models.Model):
    title = models.CharField(max_length=100, default='Title', null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    cropping = ImageRatioField('image', '1000x1000', allow_fullsize=True, size_warning=True)

    def __str__(self):
        return self.title
