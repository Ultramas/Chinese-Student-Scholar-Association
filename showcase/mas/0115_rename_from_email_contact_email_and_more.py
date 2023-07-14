# Generated by Django 4.1.2 on 2022-12-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0114_address_is_active_banappeal_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='from_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='inquiry',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.TextField(default=0, help_text='Name'),
            preserve_default=False,
        ),
    ]
