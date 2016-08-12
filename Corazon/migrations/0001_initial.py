# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 18:13
from __future__ import unicode_literals

import Corazon.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=2)),
                ('clinica', models.CharField(blank=True, max_length=30)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=Corazon.models.url)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('send_mail', 'Puede enviar mails'),),
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=2)),
                ('edad', models.PositiveIntegerField()),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorsiado'), ('V', 'Viudo')], max_length=2)),
                ('nacionalidad', models.CharField(blank=True, max_length=20)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=Corazon.models.url2)),
                ('doctor1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Corazon.Doctor')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('ver_perfil', 'Pueden ver su perfil'),),
            },
        ),
    ]