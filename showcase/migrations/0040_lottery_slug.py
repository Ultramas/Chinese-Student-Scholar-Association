# Generated by Django 4.1.10 on 2024-01-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0039_membership_alter_shuffler_demonstration_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
