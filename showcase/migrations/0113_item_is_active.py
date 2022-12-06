# Generated by Django 4.1.2 on 2022-12-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0112_changepasswordbackgroundimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_active',
            field=models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='1->Active, 0->Inactive', null=True, verbose_name='Out of stock?'),
        ),
    ]
