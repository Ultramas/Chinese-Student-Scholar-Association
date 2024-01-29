# Generated by Django 4.1.10 on 2024-01-17 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0026_alter_prizepool_options_prizepool_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shuffler',
            name='choices',
        ),
        migrations.AddField(
            model_name='shuffler',
            name='choices',
            field=models.ManyToManyField(blank=True, null=True, to='showcase.choice'),
        ),
    ]
