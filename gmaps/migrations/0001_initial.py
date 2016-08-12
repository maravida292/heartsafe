# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=80)),
                ('marcaa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pulsos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=80)),
                ('lng', models.CharField(max_length=80)),
                ('BPM', models.CharField(max_length=80)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gmaps.Device')),
            ],
        ),
    ]
