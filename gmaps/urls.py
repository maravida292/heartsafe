from django.conf.urls import patterns, url
from gmaps import views

urlpatterns = [
	url(r'^conection/', views.create_Data, name='conection'),#Url para conectar con el dispositivo

	url(r'^api/lps.dat', views.get_lps, name='get_lps'),#URL que se usa en la grafica
	url(r'^grafica/', views.verGrafica, name='verGrafica'),

	#url(r'^lngPac/(?P<id_pac>\w+)/', views.get_lng, name='get_lng'),#Url longitud y latitud obtiene en formato JSON
	url(r'^lngPac/(?P<id_pac>\w+)/', views.get_lng, name='get_lng'),#Url longitud y latitud obtiene en formato JSON
	url(r'^ver/(?P<id_pac>.*)/', views.verMapa, name='verMapa'),
]