# Generated by Django 4.1.10 on 2024-12-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0010_membership_discount_price_membership_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
