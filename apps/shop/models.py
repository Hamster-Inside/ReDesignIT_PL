from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from unidecode import unidecode


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['level']

    def save(self, *args, **kwargs):
        # Set the slug to be the same as the name, using Django's slugify function
        ascii_category_name = unidecode(self.name)
        self.slug = slugify(ascii_category_name)

        # Call the save method of the parent class (Model) to save the object
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            ascii_category_name = unidecode(self.name)
            self.slug = slugify(ascii_category_name)
        super().save(*args, **kwargs)
        new_slug = f'{slugify(self.name)}-{self.pk}'
        if self.slug != new_slug:
            self.slug = new_slug
            super().save(*args, **kwargs)
