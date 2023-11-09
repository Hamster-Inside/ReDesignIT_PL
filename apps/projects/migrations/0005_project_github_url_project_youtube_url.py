# Generated by Django 4.2.6 on 2023-11-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='project',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]