from django.conf.urls import patterns, url
from fichaMedica import views

urlpatterns = [
	url(r'^registro/paciente/(?P<id_pac>.*)/', views.ficha_medica, name='ficha_medica'),
	url(r'^pac/enfermedades/(?P<id_pac>.*)/', views.registrar_ficha_medica_tipo, {'tipoFicha': 1}, name='enfermedades'),
	url(r'^pac/cirujias/(?P<id_pac>.*)/', views.registrar_ficha_medica_tipo, {'tipoFicha': 2}, name='cirujias'),
	url(r'^pac/alergias/(?P<id_pac>.*)/', views.registrar_ficha_medica_tipo, {'tipoFicha': 3}, name='alergias'),
	url(r'^pac/tratemientos/(?P<id_pac>.*)/', views.registrar_ficha_medica_tipo, {'tipoFicha': 4}, name='tratamientos'),

	url(r'^ver/pac/(?P<id_pac>.*)/', views.ver_update_ficha, name='verUpdateFichaMedica'),
	url(r'^edit/(?P<id_fm>.*)/', views.edit_ficha, name='editFichaMedica'),


]
#Tipo ficha es el tab que usa
#1 enfermedades
#2 cirujias
#3 alergias
#4 tratemientos
