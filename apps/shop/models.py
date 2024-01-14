from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from unidecode import unidecode


class CommonFields(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, default="")

    # Add other common fields here

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ascii_name = unidecode(self.name)
        self.slug = f'{slugify(ascii_name)}-{self.pk}'
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(MPTTModel, CommonFields):
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['level']


class Product(CommonFields):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
