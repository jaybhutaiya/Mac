# Generated by Django 5.0 on 2024-01-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sega', '0004_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
