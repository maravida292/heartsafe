from __future__ import unicode_literals
from django.db import models

class Device(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=6)
	marca = models.CharField(max_length=10)
	ocupado = models.BooleanField(default=False)

	def __unicode__(self):
		return  '%s - Codigo: %s' %(self.nombre, self.codigo)

class Pulsos(models.Model):
	device = models.ForeignKey(Device)
	lat = models.CharField(max_length=80)
	lng = models.CharField(max_length=80)
	BPM = models.CharField(max_length=80)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Pulso - lat: %s, lng: %s del device: %s' %(self.lat, self.lng, self.device.nombre)
