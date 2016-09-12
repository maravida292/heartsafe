from django.conf.urls import patterns, url
from gmaps import views

urlpatterns = [
	url(r'^conection/', views.create_Data, name='conection'),#Url para conectar con el dispositivo
	url(r'^conexion2/', views.create_Data2, name='conection'),#Url para conectar con el dispositivo :)

	url(r'^api/lps.dat', views.get_lps, name='get_lps'),#URL que se usa en la grafica
	url(r'^api/grafica.dat', views.get_lps2, name='get_lps2'),#URL que se usa en la grafica del ritmo cardiaco :)

	url(r'^graficaBPM/', views.verGrafica_BPM, name='verGraficaBPM'),
	url(r'^graficaPPG/', views.verGrafica_PPG, name='verGraficaPPG'),

	url(r'^lngPac/(?P<id_pac>\w+)/', views.get_lng, name='get_lng'),#Url longitud y latitud obtiene en formato JSON
	url(r'^ver/(?P<id_pac>.*)/', views.verMapa, name='verMapa'),

	url(r'^createDevice/', views.createDevice, name='createDevice'),
	url(r'^edit/dev/(?P<id_device>.*)/', views.editDevice, name='editarDevice'),
	url(r'^delete/dev/(?P<id_device>.*)/', views.deleteDevice, name='eliminarDevice'),
	url(r'^reporte/reportexfecha/(?P<id_pac>.*)/', views.reportexFecha, name='reportexFecha'),
	url(r'^reporte/reportexPaciente/', views.reportexPacienteyFecha, name='reportexPaciente'),
	url(r'^modal/', views.modal, name='modal')
]