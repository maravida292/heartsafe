from __future__ import unicode_literals
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from Corazon.models import Paciente
from Corazon.models import Doctor

class FichaMedica(models.Model):
	TIP = (('E', 'Enfermedades'),('C', 'Cirujias'),('H', 'Hospitalizaciones'),('A', 'Alergias'),('T', 'Tratamientos'))
	TYPE_GAFAS = (('L', 'Lectura'),('P', 'Permanentes'),('N', 'No'),)
	
	paciente = models.ForeignKey(Paciente, null=True, blank=True)
	doctor = models.ForeignKey(Doctor, null=True, blank=True)
	tipo = models.CharField(max_length=1, choices=TIP, null=True, blank=True)
	detalles = models.CharField(max_length=256)
	descripcion = models.CharField(max_length=256)
	fecha = models.DateTimeField(auto_now=True)

	def __unicode__(self):		
		return '%s Fecha de elaboracion: %s' % (self.paciente.usuario.username, self.fecha)
