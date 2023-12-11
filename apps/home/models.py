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


class Statistic(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_count = models.PositiveIntegerField(default=1)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    continent = models.CharField(max_length=20, default='Unknown')
    country = models.CharField(max_length=100, default='Unknown')
    city = models.CharField(max_length=150, default='Unknown')

    def __str__(self):
        return f"{self.ip_address}"
