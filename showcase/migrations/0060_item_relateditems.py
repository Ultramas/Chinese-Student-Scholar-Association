# Generated by Django 3.2.11 on 2022-03-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0059_userprofile2_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='relateditems',
            field=models.ManyToManyField(related_name='_showcase_item_relateditems_+', to='showcase.Item'),
        ),
    ]
