from django.db import models


# Create your models here.

class ProgrammingLanguage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    programming_language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.programming_language_name


class Framework(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    framework_name = models.CharField(max_length=50)

    def __str__(self):
        return self.framework_name


class WebProfile(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    profile_name = models.CharField(max_length=50)
    profile_url = models.CharField(max_length=300)

    def __str__(self):
        return self.profile_name


class MyApp(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.name
