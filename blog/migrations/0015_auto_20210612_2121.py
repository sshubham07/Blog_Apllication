# Generated by Django 3.0.2 on 2021-06-12 15:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_myblog_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyBlog',
            new_name='Article',
        ),
    ]
