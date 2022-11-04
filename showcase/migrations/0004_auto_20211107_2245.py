# Generated by Django 3.1.5 on 2021-11-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_showcasepost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name goes here.', max_length=100)),
                ('catagory', models.CharField(help_text='Choose a catagory you want your idea to affect (server layout, event idea, etc).', max_length=100)),
                ('description', models.TextField(help_text='Please share any ideas you may have.')),
                ('image', models.FileField(help_text='Please give us a picture that represents your idea. It does not have to be exact.', upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name goes here.', max_length=100)),
                ('catagory', models.CharField(help_text='Choose a catagory you want your idea to affect (server layout, event idea, etc).', max_length=100)),
                ('description', models.TextField(help_text='Please share any ideas you may have.')),
                ('image', models.FileField(help_text='Please give us a picture that represents your idea. It does not have to be exact.', upload_to='gallery')),
            ],
        ),
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.FileField(help_text='Upload a picture for your profile (scales to your picture`s dimensions.)', upload_to='gallery'),
        ),
    ]
