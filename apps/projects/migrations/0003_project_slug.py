# Generated by Django 4.2.6 on 2023-11-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_project_name_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]