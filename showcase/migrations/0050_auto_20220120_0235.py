# Generated by Django 3.1.5 on 2022-01-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0049_auto_20220120_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
