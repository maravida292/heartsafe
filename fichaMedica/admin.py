from django.contrib import admin
from .models import *

class FichaMedicaAdmin(admin.ModelAdmin):
	list_display = ('id','paciente', 'doctor', 'tipo','fecha')#como se muestra las columnas
	list_filter = ('paciente', 'fecha')#filtrado de Ficha Medica por nombre de usuario y cedula


admin.site.register(FichaMedica, FichaMedicaAdmin)