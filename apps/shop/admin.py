from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Category, Product


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
