# Generated by Django 4.2.6 on 2023-11-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_programming_language_programminglanguage_programming_language_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
    ]