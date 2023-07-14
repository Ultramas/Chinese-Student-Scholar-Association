# Generated by Django 4.1.2 on 2023-07-02 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0012_alter_updateprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateprofile',
            name='image',
            field=models.ImageField(default=1, help_text='Attach an image for your profile (scales to your picture`s dimensions.)', upload_to=''),
            preserve_default=False,
        ),
    ]
