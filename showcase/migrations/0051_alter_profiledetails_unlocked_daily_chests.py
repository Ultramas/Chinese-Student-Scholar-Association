# Generated by Django 4.1.10 on 2024-12-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0050_remove_profiledetails_unlocked_daily_chests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='unlocked_daily_chests',
            field=models.ManyToManyField(null=True, to='showcase.game'),
        ),
    ]
