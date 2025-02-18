# Generated by Django 4.1.10 on 2024-12-24 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0066_inventoryobject_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='prizepool',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='showcase.currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prizepool',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
