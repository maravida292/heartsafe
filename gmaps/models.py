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
	ACCEPTED_FORMATS = ['%Y-%m-%d']
	device = models.ForeignKey(Device)
	lat = models.CharField(max_length=80)
	lng = models.CharField(max_length=80)
	BPM = models.CharField(max_length=8)
	fecha = models.DateField(auto_now_add=True, blank=True)
	hora = models.TimeField(blank=True, default=datetime.now().strftime('%H:%M:%S'))

	def __unicode__(self):
		return 'Pulso - lat: %s, lng: %s del device: %s' %(self.lat, self.lng, self.device.nombre)

class Grafica(models.Model):
	# pulso = models.OneToOneField(Pulsos)
	t1 = models.IntegerField(blank=True)
	t2 = models.IntegerField(blank=True)
	p1 = models.IntegerField(blank=True)
	p2 = models.IntegerField(blank=True)
	IBI = models.IntegerField(blank=True)


