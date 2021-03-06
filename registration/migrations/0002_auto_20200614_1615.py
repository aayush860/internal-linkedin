# Generated by Django 3.0.7 on 2020-06-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='Password',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signin',
            name='Username',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Email',
            field=models.EmailField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='FullName',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='MobileNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Password',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Username',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
