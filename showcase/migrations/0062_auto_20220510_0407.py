# Generated by Django 3.2.11 on 2022-05-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0061_alter_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".', max_length=100)),
                ('catagory', models.CharField(help_text='Please let us know what type of issue you are dealing with.', max_length=200)),
                ('issue', models.TextField(help_text='Describe your issue in detail. We will try to get back to you as soon as possible.')),
                ('Additional_comments', models.TextField(help_text='Put any additional comments you may have here.')),
                ('image', models.URLField(help_text='Please attach a screenshot of your issue.')),
            ],
            options={
                'verbose_name': 'Customer Support',
                'verbose_name_plural': 'Customer Support',
            },
        ),
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)', upload_to=''),
        ),
    ]
