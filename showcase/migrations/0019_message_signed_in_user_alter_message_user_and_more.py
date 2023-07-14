# Generated by Django 4.1.2 on 2023-07-05 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0018_remove_profiledetails_link_to_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='signed_in_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='userprofile2',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
