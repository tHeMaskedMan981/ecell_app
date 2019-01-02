# Generated by Django 2.0.5 on 2019-01-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='category',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='speaker',
            old_name='link',
            new_name='limkedin_link',
        ),
        migrations.RenameField(
            model_name='speaker',
            old_name='photo',
            new_name='photo_url',
        ),
        migrations.AddField(
            model_name='speaker',
            name='designation',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
