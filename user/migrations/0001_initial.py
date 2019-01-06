# Generated by Django 2.0.5 on 2019-01-06 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('session_token', models.CharField(blank=True, editable=False, max_length=64, null=True)),
            ],
            options={
                'db_table': 'user_login',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('esummit_id', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(choices=[('student', 'student'), ('professional', 'professional'), ('entrepreneur', 'entrepreneur')], default='student', max_length=20)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('photo_url', models.URLField(blank=True, default=None, null=True)),
                ('user_events', models.ManyToManyField(blank=True, default=None, to='events.Event')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
