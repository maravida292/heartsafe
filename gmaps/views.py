from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import json


#Importacion de los modelos
from eventlog.models import log
from gmaps.models import Device
from gmaps.forms import *
from Corazon.models import Paciente



@login_required
def verMapa(request, id_pac):
    return render_to_response("verMapa.html", {"id_pac" : id_pac}, context_instance=RequestContext(request))

@login_required
def verGrafica(request):
    return render_to_response("verGrafica.html", context_instance=RequestContext(request))


@csrf_exempt
def create_Data(request):##Funcion para receptar los datos sensados del corazon y la ubicacion
	"""
	BPM, LATITUD, LONGITUD :param request:
	JSON :return:
	"""
	id_dispo = request.GET.get("id_dispo")
	latitud = request.GET.get("latitud")
	longitud = request.GET.get("longitud")
	pulso = request.GET.get("pulso")

	p = Pulsos()
	p.device = Device.objects.get(codigo=id_dispo)
	p.lng = longitud
	p.lat = latitud
	p.BPM = pulso
	p.save()
	return HttpResponse("True")


@csrf_exempt
def get_lps(request):#Funcion para graficas
	try:
		id_dispo = request.POST.get("id_dispo")
		pulsos = Pulsos.objects.filter(device=Device.objects.get(codigo=id_dispo))
		total = len(pulsos)
		ult_pulso = pulsos[total-1]
		ult_pulso = ult_pulso.BPM

	except:
		ult_pulso = 0

	return HttpResponse(ult_pulso)

@csrf_exempt
def get_lng(request, id_pac):#Funcion para obtener lista de ubicacion JSON del mapa
	print(id_pac)
	paciente = Paciente.objects.get(id=id_pac)
	ubicacion_por_paciente = Pulsos.objects.filter(device=paciente.devide1)
	print (ubicacion_por_paciente)
	ubicacion_list = map( lambda x: dict(
		id = x.id,
		device = x.device.codigo,
		lat = float(x.lat),
		lng = float(x.lng),
		), ubicacion_por_paciente)
	return HttpResponse(json.dumps(ubicacion_list), content_type='application/json')


def createDevice(request):
	if request.method == 'POST':
		form = DeviceForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'DEVICE AGREGADO CON EXITO.')
			context = {"titulo": "Crear Device"}
		else:
			context = {"titulo": "Crear Device", "form": form}
	else:  # GET
		form = DeviceForm()
		context = {"titulo": "Crear Device", "form": form}
	return render(request, "registrar.html", context)


def editDevice(request, id_device):
	device = Device.objects.get(id=id_device)
	if request.method == 'POST':
		form = DeviceForm(request.POST, request.FILES, instance=device)
		if (form.is_valid()):
			form.save()
			return redirect('administrador')
	else:
		form = DeviceForm(instance=device)
	context = {'form': form,'titulo': "Dispositivo"}
	return render_to_response("paciente_edit.html", context, context_instance=RequestContext(request))



def deleteDevice(request, id_device):
	usuario = request.user
	device = Device.objects.get(id=id_device)
	if request.method == 'POST':
		log(user=usuario, action='ELIMINAR DEVICE',
			extra={"Device_Eliminado": device.nombre, "Quien_lo_elimino": usuario.username})
		device.delete()
		return redirect('administrador')  # Se redirige a la url q tiene como nombre administrador
	return render(request, 'deletePD.html', {'item_eliminar': device.nombre})


