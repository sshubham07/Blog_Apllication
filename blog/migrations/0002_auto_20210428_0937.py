# Generated by Django 3.0.8 on 2021-04-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
