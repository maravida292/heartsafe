from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Notification
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from Corazon.models import *

# Create your views here.


def verMensaje(request, id_noti):
	n = Notification.objects.get(id=id_noti)
	if request.method == "POST":
		form = showMensajeDP(request.POST, instance=n)
		if form.is_valid():
			instancia = form.save(commit=False)
			instancia.leido = True;
			instancia.save()
			context = {"titulo": "MENSAJE ENVIADO CORRECTAMENTE"}
	else:
		form = showMensajeDP(instance=n)
		context = {"titulo": "Ver mensaje.", "form": form}
	return render(request, "notification.html", context)


def showALLNotification(request):
	notification = Notification.objects.filter(user1=request.user)
	context = {
		"notification": notification,
		}
	return render(request, "verMensajes.html",context)

def enviarMsjalPaciente(request, id_pac):
	userActual = request.user
	paciente = Paciente.objects.get(id=id_pac)
	user1 = User.objects.get(id = paciente.usuario.id)

	if request.method == 'POST':
		form = FormMsjToPaciente(request.POST)
		if form.is_valid():
			instancia = form.save(commit=False)  # instancia es un objeto Notificacion
			instancia.user1 = user1
			instancia.user_envio = "%s %s (%s)" % (userActual.first_name, userActual.last_name, userActual.username)
			instancia.tipon = 'M'
			instancia.save()
			messages.add_message(request, messages.INFO, 'Mensaje enviado con exito.')  # MESSAGES DESPUES DE AGREGAR PAC

			context = {
				"titulo": "Enviar otro mensaje."
			}
	else:  # GET
		form = FormMsjToPaciente()
		context = {"titulo" : "Enviar Mensaje", "form": form}
	return render(request, "sendMsj.html", context)




#Enviar mensaje general eligiendo el paciente o doctor segun sea el caso
def enviarMensajePD(request):
	user = request.user
	if user.groups.filter(name='Pacientes').exists():
		doctorid = Doctor.objects.get(id = user.paciente.doctor1.id)
		userid = doctorid.usuario.id
		form = MensajeFormPaciente(request.POST or None, userid=userid)
	if user.groups.filter(name='Doctores').exists():
		doctorid2 = user.doctor.id
		form = MensajeFormDoctor(request.POST or None, userid=doctorid2)
	
	context = {
		"titulo": "Enviar Mensaje",
		"form": form }


	if form.is_valid():
		instancia = form.save(commit=False)#instancia es un objeto Notificacion
		instancia.user_envio = "%s %s (%s)" %(user.first_name, user.last_name, user.username)
		instancia.tipon = 'M'
		instancia.save()
		messages.add_message(request, messages.INFO, 'Mensaje enviado con exito.' )#MESSAGES DESPUES DE AGREGAR PAC

		context = {
			"titulo": "Enviar otro mensaje.",
			"referencia": "/notification/verMensajes"
		}

	return render(request, "sendMsj.html", context)

def messageOfUser(request):
	user = request.user
	lista_mensajes = Notification.objects.filter(user1=user, tipon='M', leido=False)
	return render(request, "notifications-menu.html", locals())