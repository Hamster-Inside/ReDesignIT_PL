from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_text = models.TextField()
    contact_email = models.CharField(max_length=100)

    def __str__(self):
        return 'Contact Me'
