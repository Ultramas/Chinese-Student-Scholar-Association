# Generated by Django 4.1.10 on 2024-08-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0008_alter_withdraw_options_withdraw_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='withdraw',
            options={'verbose_name': 'Withdrawal Card', 'verbose_name_plural': 'Withdrawal Cards'},
        ),
        migrations.RemoveField(
            model_name='withdraw',
            name='image',
        ),
        migrations.RemoveField(
            model_name='withdrawclass',
            name='currency',
        ),
        migrations.AlterField(
            model_name='withdrawclass',
            name='fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
