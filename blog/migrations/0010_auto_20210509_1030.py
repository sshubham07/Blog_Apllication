# Generated by Django 3.0.8 on 2021-05-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210509_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]