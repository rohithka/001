# Generated by Django 2.2.8 on 2022-10-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20221028_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournamentmodel',
            old_name='slot_available',
            new_name='team_space_available',
        ),
        migrations.RenameField(
            model_name='tournamentmodel',
            old_name='slots',
            new_name='teams',
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='slots',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='09:00:39'),
        ),
    ]
