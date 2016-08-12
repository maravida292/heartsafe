from django.contrib import admin
from .models import *

class FichaMedicaAdmin(admin.ModelAdmin):
	list_display = ('id','paciente', 'doctor', 'tipo','fecha')#como se muestra las columnas
	search_fields = ('paciente__usuario__username', 'fecha')#filtrado de Ficha Medica por nombre de usuario y cedula


admin.site.register(FichaMedica, FichaMedicaAdmin)