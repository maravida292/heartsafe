# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0002_notification_tipon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='mensaje',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='notification',
            name='titulo',
            field=models.CharField(max_length=80),
        ),
    ]
