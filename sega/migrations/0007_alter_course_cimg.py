# Generated by Django 5.0 on 2024-01-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sega', '0006_course_bi_course_cimg_course_cinfo_course_cname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cimg',
            field=models.ImageField(upload_to='images/'),
        ),
    ]