# Generated by Django 3.2.6 on 2021-08-06 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_contact',
        ),
        migrations.AddField(
            model_name='client',
            name='client_phone',
            field=models.CharField(default=2, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
            preserve_default=False,
        ),
    ]
