# Generated by Django 4.1.2 on 2023-07-08 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0023_alter_message_signed_in_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='hyperlink',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
