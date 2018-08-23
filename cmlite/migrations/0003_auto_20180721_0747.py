# Generated by Django 2.0.7 on 2018-07-21 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmlite', '0002_auto_20180720_0705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='title',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(default='..', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='..', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]