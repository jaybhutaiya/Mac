# Generated by Django 5.0 on 2024-01-25 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sega', '0002_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
    ]
