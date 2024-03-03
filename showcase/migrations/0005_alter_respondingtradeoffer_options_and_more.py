# Generated by Django 4.1.10 on 2024-03-01 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0004_alter_respondingtradeoffer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respondingtradeoffer',
            options={'verbose_name': 'Trade Offer Response', 'verbose_name_plural': 'Trade Offer Responses'},
        ),
        migrations.RemoveField(
            model_name='respondingtradeoffer',
            name='offered_trade_items',
        ),
        migrations.AlterField(
            model_name='respondingtradeoffer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dealer', to=settings.AUTH_USER_MODEL, verbose_name='Dealer'),
        ),
        migrations.RemoveField(
            model_name='respondingtradeoffer',
            name='wanted_trade_items',
        ),
        migrations.AddField(
            model_name='respondingtradeoffer',
            name='offered_trade_items',
            field=models.ManyToManyField(to='showcase.tradeitem'),
        ),
        migrations.AddField(
            model_name='respondingtradeoffer',
            name='wanted_trade_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.tradeoffer'),
        ),
    ]
