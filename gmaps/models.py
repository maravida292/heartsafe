from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Device(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=6)
	marca = models.CharField(max_length=10)
	ocupado = models.BooleanField(default=False)

	def __unicode__(self):
		return  '%s - Codigo: %s' %(self.nombre, self.codigo)

class Pulsos(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	lat = models.CharField(max_length=80)
	lng = models.CharField(max_length=80)
	BPM = models.CharField(max_length=8)
	fecha = models.DateField(auto_now_add=True, blank=True)
	hora = models.TimeField(blank=True, default=datetime.now().strftime('%H:%M:%S'))

	def __unicode__(self):
		return 'Pulso - lat: %s, lng: %s del device: %s' %(self.lat, self.lng, self.device.nombre)

class Grafica(models.Model):
	pulso = models.OneToOneField(Pulsos, null=True, blank=True)
	valles = models.CharField(max_length=8, blank=True)
	picos = models.CharField(max_length=8, blank=True)
	estable = models.CharField(max_length=8, blank=True)
	periodo = models.CharField(max_length=8, blank=True)#Periodo dado en mili-segundos

	def __unicode__(self):
		return 'Grafica del device: %s del BPM %s' % (self.pulso.device.nombre, self.pulso.BPM)


