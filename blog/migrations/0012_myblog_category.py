# Generated by Django 3.0.8 on 2021-05-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210531_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='category',
            field=models.CharField(choices=[('politics', 'politics'), ('Sports', 'Sports'), ('Busines', 'Busines'), ('Education', 'Education'), ('Other', 'Other')], default='Other', max_length=15),
        ),
    ]
