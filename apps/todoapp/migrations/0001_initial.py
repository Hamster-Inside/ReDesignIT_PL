# Generated by Django 4.2.6 on 2023-11-13 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list_name', models.CharField(default='New Todo List', max_length=100)),
                ('slug', models.SlugField(default='', unique=True)),
                ('todo_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Title', max_length=100)),
                ('description', models.TextField(default='NULL Description')),
                ('is_done', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='', unique=True)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todolist')),
            ],
        ),
    ]
