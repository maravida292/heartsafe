# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from gmaps.models import *



class DeviceForm(forms.ModelForm):
	nombre = forms.CharField(max_length=100, required=True, widget=forms.TextInput(), help_text='Device1')
	codigo = forms.CharField(max_length=6, required=True, widget=forms.TextInput(), help_text='Ejm: 12345', label='Código')
	marca = forms.CharField(max_length=10, required=True, widget=forms.TextInput())

	class Meta:
		model = Device
		fields = ['nombre', 'codigo', 'marca']

	def clean_codigo(self):
		codigo = self.cleaned_data.get('codigo')
		if not (codigo.isdigit()):
			raise forms.ValidationError("Ingrese numeros.")
		return codigo