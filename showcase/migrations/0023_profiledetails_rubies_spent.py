# Generated by Django 4.1.10 on 2024-12-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0022_monstrosity_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='rubies_spent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
