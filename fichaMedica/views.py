from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import *
from Corazon.models import *
from django.contrib import messages
from fichaMedica.forms import *

#instancia.tipo = 'E' Enfermedades
#'C', 'Cirujias'
#'H', 'Hospitalizaciones'
#'A', 'Alergias'


def registrar_ficha_medica_tipo(request, id_pac, tipoFicha):
	userActual = request.user
	if userActual.groups.filter(name='Doctores').exists():
		doctor = Doctor.objects.get(id=userActual.doctor.id)
	paciente = Paciente.objects.get(id=id_pac)

	if (tipoFicha == 1):
		enfermedades = True
		tipoForm = 'E'
		titulo1 = "Registrar ficha medica - Enfermedades"
	if (tipoFicha == 2):
		enfermedades = True
		tipoForm = 'C'
		titulo1 = "Registrar ficha medica - Cirujias"
	if (tipoFicha == 3):
		enfermedades = True
		tipoForm = 'A'
		titulo1 = "Registrar ficha medica - Alergias"
	if (tipoFicha == 4):
		enfermedades = True
		tipoForm = 'T'
		titulo1 = "Registrar ficha medica - Tratamientos"

	if request.method == 'POST':
		form = ficha_MedicaForm(request.POST or None)
		if form.is_valid():
			instancia = form.save(commit=False)
			instancia.paciente = paciente
			instancia.doctor = doctor
			instancia.tipo = tipoForm
			instancia.save()
			messages.add_message(request, messages.INFO, 'FICHA MEDICA AGREGADA')  # MESSAGES DESPUES DE AGREGAR FICHA MEDICA

			context = {"titulo2": "Registrar otro reporte de ficha medica. Click aqui. ", 'doctor':doctor,
					   "enfermedades": enfermedades, "paciente": paciente}
	else:  # GET
		form = ficha_MedicaForm()
		#Se comprueba que existe el doctor y se lo manda en el contexto
		context = {"titulo1": titulo1, "form": form, 'doctor':doctor,
				   "paciente": paciente,"enfermedades": enfermedades}
	return render(request, "tabsFichaMedica.html", context)




def ficha_medica(request, id_pac):
	userActual = request.user
	if userActual.groups.filter(name='Doctores').exists():
		doctor = Doctor.objects.get(id=userActual.doctor.id)
	paciente = Paciente.objects.get(id=id_pac)
	return render (request, "fichaMedica.html", {'paciente' : paciente, 'doctor': doctor})


def ver_update_ficha(request, id_pac):
	paciente1 = FichaMedica.objects.get(id=id_pac)
	ficha1 = FichaMedica.objects.get(id=11)
	if request.method == "POST":
		form = ficha_MedicaForm(request.POST, instance=ficha1)
		if form.is_valid():
			form.save()
			return redirect('administrador')
	else:
		form = ficha_MedicaForm(instance=ficha1)
	context = {'form': form}
	return render_to_response("verFichaMedica.html", context, context_instance=RequestContext(request))


