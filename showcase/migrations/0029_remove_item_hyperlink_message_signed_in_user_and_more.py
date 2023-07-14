# Generated by Django 4.1.2 on 2023-07-09 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0028_remove_message_signed_in_user_item_hyperlink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='hyperlink',
        ),
        migrations.AddField(
            model_name='message',
            name='signed_in_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='hyperlink',
            field=models.CharField(default=1, help_text='Leave field blank, hyperlink will automatically fill with the link to the associated product.', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='slug',
            field=models.SlugField(default=1, help_text='Leave blank to use corresponding product slug.', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000, verbose_name='Username'),
        ),
    ]
