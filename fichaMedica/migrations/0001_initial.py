# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Corazon', '0002_auto_20160719_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('E', 'Enfermedades'), ('C', 'Cirujias'), ('H', 'Hospitalizaciones'), ('A', 'Alergias'), ('T', 'Tratamientos')], max_length=1, null=True)),
                ('sintomas', models.CharField(max_length=256)),
                ('diagnostico', models.CharField(max_length=256)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Corazon.Doctor')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Corazon.Paciente')),
            ],
        ),
    ]