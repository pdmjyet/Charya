# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 19:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GoalApp', '0002_auto_20180126_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 19, 48, 53, 193982, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 19, 48, 53, 195022, tzinfo=utc)),
        ),
    ]