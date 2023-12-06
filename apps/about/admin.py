from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import About, AboutImage


# Register your models here.

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(About)
admin.site.register(AboutImage, MyModelAdmin)
