# Generated by Django 4.1.10 on 2024-08-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0023_profiledetails_times_subtract_called_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='black_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='gold_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='green_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='orange_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='red_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='redgold_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='yellow_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='black_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='gold_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='green_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='orange_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='red_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='red_gold_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='yellow_cards_hit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
