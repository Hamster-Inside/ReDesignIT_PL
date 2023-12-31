# Generated by Django 4.2.6 on 2023-12-06 12:30

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutimages',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '1000x1000', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
    ]
