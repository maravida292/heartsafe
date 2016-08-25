from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Notification(models.Model):
	TIPO = (('M', 'Mensaje'), ('A', 'Alertas'), ('N', 'Notificacion'))
	titulo = models.CharField(max_length=80)
	mensaje = models.TextField(blank=True)
	leido = models.BooleanField(default=False)
	user1 = models.ForeignKey(User, on_delete=models.CASCADE)
	user_envio = models.CharField(max_length=50, blank=True, null=True)
	tipon = models.CharField(max_length=1, choices=TIPO, null=True, blank=True)#Tipo de notificacion
	fecha_noti = models.DateTimeField(auto_now=True, blank=True)

	def __unicode__(self):		
		return '%s Asunto:%s' % (self.user1.username, self.titulo)