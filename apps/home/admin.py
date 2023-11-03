from django.contrib import admin
from .models import ProgrammingLanguage, Framework, WebProfile

# Register your models here.
admin.site.register(ProgrammingLanguage)
admin.site.register(Framework)
admin.site.register(WebProfile)
