# Generated by Django 4.2.6 on 2023-11-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_author_alter_task_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taskgroup',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]