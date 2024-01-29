# Generated by Django 4.1.10 on 2024-01-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0041_remove_lottery_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
