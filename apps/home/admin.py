from django.contrib import admin
from .models import ProgrammingLanguage, Framework, WebProfile, MyApp

# Register your models here.
admin.site.register(ProgrammingLanguage)
admin.site.register(Framework)
admin.site.register(WebProfile)
admin.site.register(MyApp)
