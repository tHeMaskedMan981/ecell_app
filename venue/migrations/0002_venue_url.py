# Generated by Django 2.0.5 on 2018-12-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
