# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0002_schedule_dk_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='dk_event_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='fee',
            field=models.FloatField(null=True),
        ),
    ]