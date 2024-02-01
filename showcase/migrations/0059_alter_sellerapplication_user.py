# Generated by Django 4.1.10 on 2024-01-30 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0058_profiledetails_seller_sellerapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerapplication',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
