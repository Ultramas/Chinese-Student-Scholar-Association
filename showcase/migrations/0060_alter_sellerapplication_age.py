# Generated by Django 4.1.10 on 2024-01-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0059_alter_sellerapplication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerapplication',
            name='age',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]
