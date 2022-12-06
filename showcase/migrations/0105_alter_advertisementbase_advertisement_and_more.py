# Generated by Django 4.1.2 on 2022-11-26 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0104_remove_advertisementbase_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementbase',
            name='advertisement',
            field=models.ImageField(help_text='Image of the advertisement.', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='faviconbase',
            name='faviconcover',
            field=models.ImageField(upload_to='images/', verbose_name='Favicon'),
        ),
        migrations.AlterField(
            model_name='logobase',
            name='logocover',
            field=models.ImageField(upload_to='images/', verbose_name='Logo'),
        ),
    ]
