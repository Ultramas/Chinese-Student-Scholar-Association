# Generated by Django 4.1.10 on 2024-12-09 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0012_alter_membership_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.membership'),
        ),
    ]
