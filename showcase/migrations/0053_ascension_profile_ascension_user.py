# Generated by Django 4.1.10 on 2024-12-19 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0052_alter_profiledetails_unlocked_daily_chests'),
    ]

    operations = [
        migrations.AddField(
            model_name='ascension',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='showcase.profiledetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ascension',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
