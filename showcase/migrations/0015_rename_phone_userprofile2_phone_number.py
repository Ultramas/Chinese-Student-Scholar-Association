# Generated by Django 4.1.10 on 2024-03-07 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0014_userprofile2_zip_code_alter_userprofile2_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile2',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
