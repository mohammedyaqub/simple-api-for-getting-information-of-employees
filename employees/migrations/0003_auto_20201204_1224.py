# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-12-04 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20201203_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='challenge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='done',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='quality_check',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='working',
            field=models.TextField(blank=True, null=True),
        ),
    ]
