# Generated by Django 4.1.10 on 2024-12-27 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0071_notification_inventorytradeoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleparticipant',
            name='battle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='battle_joined', to='showcase.battle'),
        ),
    ]
