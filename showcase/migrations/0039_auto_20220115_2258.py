# Generated by Django 3.1.5 on 2022-01-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0038_auto_20220114_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(help_text='Link a URL for your idea (scales to your picture`s dimensions.)'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='image',
            field=models.URLField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)'),
        ),
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.URLField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)'),
        ),
    ]
