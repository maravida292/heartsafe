# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import *


class ficha_MedicaForm(forms.ModelForm):
	detalles = forms.CharField(max_length=200, label='Detalles', widget=forms.Textarea)
	descripcion = forms.CharField(max_length=200, label='Descripción', widget=forms.Textarea)

	class Meta:
		model   = FichaMedica
		fields = ['detalles','descripcion']
		exclude = {'paciente', 'doctor', 'tipo', "fecha_noti"}

	def clean(self):
		print self.cleaned_data
		return self.cleaned_data

class ficha_MedicaForm2(forms.ModelForm):
	detalles = forms.CharField(max_length=200)
	descripcion = forms.CharField(max_length=200)

	class Meta:
		model   = FichaMedica
		fields = ['detalles','descripcion']
		exclude = {'paciente', 'doctor', 'tipo', "fecha_noti"}
