# Generated by Django 4.1.10 on 2024-12-09 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0011_membership_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
