# Generated by Django 4.1.10 on 2024-01-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0017_alter_shuffletype_circumstance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='nodes',
            field=models.IntegerField(blank=True, help_text='Number of the choice included', null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='nonce',
            field=models.DecimalField(blank=True, decimal_places=0, help_text='Nonce of choice', max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='playerversusplayer',
            name='privacy',
            field=models.CharField(choices=[('PUB', 'Public'), ('PRI', 'Private')], max_length=3),
        ),
    ]
