from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, CategoryAdmin)
