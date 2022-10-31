# Generated by Django 2.2.8 on 2022-10-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creatematchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('nos', models.IntegerField()),
                ('avs', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MatchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('locality', models.CharField(max_length=30, null=True)),
                ('creator', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(default='Upcoming', max_length=30)),
                ('slots', models.IntegerField(default=1)),
                ('slot_available', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('phoneno', models.CharField(default=7414414141, max_length=16)),
                ('status', models.CharField(default='Pending', max_length=30)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('locality', models.CharField(max_length=30, null=True)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.MatchModel')),
            ],
        ),
    ]