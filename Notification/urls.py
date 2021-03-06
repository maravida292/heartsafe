from django.conf.urls import patterns, url
from Notification import views


urlpatterns = [
	url(r'^verMensajes/', views.showALLNotification, name='ver_Mensajes'),
	url(r'^ver/(?P<id_noti>.*)/', views.verMensaje, name='ver_notification'),
	url(r'^enviarMensaje/', views.enviarMensajePD, name='enviar_Mensaje'),
	url(r'^msjPaciente/(?P<id_pac>.*)/', views.enviarMsjalPaciente, name='msj_paciente'),
	url(r'^noti/', views.messageOfUser, name='noti'),
]