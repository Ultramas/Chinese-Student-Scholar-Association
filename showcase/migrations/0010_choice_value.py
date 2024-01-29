# Generated by Django 4.1.10 on 2024-01-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0009_alter_choice_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of item in Rubicoins.', max_digits=12, null=True, verbose_name='Value (Rubicoins)'),
        ),
    ]
