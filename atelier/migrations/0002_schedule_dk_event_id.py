# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='dk_event_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]