# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0005_auto_20160819_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='fecha',
            new_name='fecha_noti',
        ),
    ]
