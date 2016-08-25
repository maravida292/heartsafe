from django import forms
from django.contrib.auth.models import User
from .models import Notification
from Corazon.models import Doctor, Paciente

class showMensajeDP(forms.ModelForm):
	class Meta:
		model = Notification
		fields = ['user_envio','titulo','mensaje']
		exclude = {'user1','leido'}

class MensajeFormPaciente(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		userid = kwargs.pop('userid')
		super(MensajeFormPaciente, self).__init__(*args, **kwargs)
		self.fields['user1'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(id=userid), label='Doctor')

	class Meta:
		model   = Notification
		fields = ['user1','titulo','mensaje']
		exclude = {'leido', 'user_envio', 'fecha_noti'}


class MensajeFormDoctor(forms.ModelForm):#Doctor quiera enviar msj a sus pacientes

	def __init__(self, *args, **kwargs):
		userid = kwargs.pop('userid')
		super(MensajeFormDoctor, self).__init__(*args, **kwargs)
		self.fields['user1'] = forms.ModelChoiceField(required=False, queryset=User.objects.filter(paciente__doctor1__id=userid), label='Paciente')

	class Meta:
		model   = Notification
		fields = ['user1','titulo','mensaje']
		exclude = {'leido', 'user_envio', 'fecha_noti'}


class FormMsjToPaciente(forms.ModelForm):
	class Meta:
		model = Notification
		fields = ['titulo', 'mensaje']
		exclude = {'user1', 'fecha_noti', 'leido', 'user_envio'}
