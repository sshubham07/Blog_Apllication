# Generated by Django 3.0.8 on 2021-05-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210503_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]