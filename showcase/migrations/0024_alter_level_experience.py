# Generated by Django 4.1.10 on 2024-12-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0023_profiledetails_rubies_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
