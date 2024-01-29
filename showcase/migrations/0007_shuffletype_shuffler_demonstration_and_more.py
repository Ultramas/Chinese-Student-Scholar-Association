# Generated by Django 4.1.10 on 2024-01-10 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0006_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShuffleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Pack Opening', max_length=200)),
                ('type', models.CharField(default='L', max_length=1, verbose_name=(('L', 'Luck'), ('S', 'Skill'), ('G', 'Grade')))),
                ('circumstance', models.CharField(default='OP', max_length=3, verbose_name=(('OP', 'One Player'), ('PVP', 'Player Versus Player'), ('MP', 'Multiple Players'), ('T', 'Tournament'), ('OE', 'Other Event'), ('L', 'Limited'), ('D', 'Drop')))),
            ],
            options={
                'verbose_name': 'Shuffle Type',
                'verbose_name_plural': 'Shuffle Types',
            },
        ),
        migrations.AddField(
            model_name='shuffler',
            name='demonstration',
            field=models.CharField(blank=True, choices=[('P', 'Practice'), ('R', 'Real'), ('DN', 'Double_Or_Nothing')], max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='PlayerVersusPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Pack Opening', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Player Versus Player',
                'verbose_name_plural': 'Player Versus Players',
            },
        ),
        migrations.AddField(
            model_name='shuffler',
            name='shuffletype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='showcase.shuffletype'),
            preserve_default=False,
        ),
    ]
