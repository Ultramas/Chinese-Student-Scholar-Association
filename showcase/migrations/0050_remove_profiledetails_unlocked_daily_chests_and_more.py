# Generated by Django 4.1.10 on 2024-12-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0049_profiledetails_unlocked_daily_chests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiledetails',
            name='unlocked_daily_chests',
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='unlocked_daily_chests',
            field=models.ManyToManyField(to='showcase.game'),
        ),
    ]
