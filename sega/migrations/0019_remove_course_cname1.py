# Generated by Django 5.0 on 2024-02-28 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sega', '0018_remove_course_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cname1',
        ),
    ]
