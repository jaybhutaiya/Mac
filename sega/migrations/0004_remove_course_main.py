# Generated by Django 5.0 on 2024-02-29 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sega', '0003_course_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='main',
        ),
    ]