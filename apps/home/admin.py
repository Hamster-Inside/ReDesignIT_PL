from django.contrib import admin
from .models import ProgrammingLanguage, Framework, Profiles

# Register your models here.
admin.site.register(ProgrammingLanguage)
admin.site.register(Framework)
admin.site.register(Profiles)
