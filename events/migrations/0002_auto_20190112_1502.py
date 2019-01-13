# Generated by Django 2.0.5 on 2019-01-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.CharField(choices=[('day1', 'day1'), ('DAY2', 'DAY2')], default='day1', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='highlight',
            field=models.BooleanField(default=False),
        ),
    ]
