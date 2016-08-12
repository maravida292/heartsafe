from __future__ import unicode_literals
from django.db import models

class Device(models.Model):
	nombre = models.CharField(max_length=200)
	codigo = models.CharField(max_length=80)
	marcaa = models.CharField(max_length=50)

	def __unicode__(self):
		return  self.nombre

class Pulsos(models.Model):
	device = models.ForeignKey(Device)
	lat = models.CharField(max_length=80)
	lng = models.CharField(max_length=80)
	BPM = models.CharField(max_length=80)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Device: %s' %self.device.nombre
