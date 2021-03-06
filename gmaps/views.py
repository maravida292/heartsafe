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
from datetime import datetime, timedelta, time
from gmaps.models import Device, Pulsos, Grafica
from Corazon.models import Paciente
from gmaps.forms import *



@login_required
def verMapa(request, id_pac):
    return render_to_response("verMapa.html", {"id_pac" : id_pac}, context_instance=RequestContext(request))

@login_required
def verGrafica_BPM(request):
    return render_to_response("graficaBPM.html", context_instance=RequestContext(request))

@login_required
def verGrafica_PPG(request):
    return render_to_response("graficaPPG.html", context_instance=RequestContext(request))


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
def create_Data2(request):##Funcion para receptar los datos sensados del corazon y la ubicacion 2
	id_dispo = request.GET.get("id_dispo")
	latitud = request.GET.get("latitud")
	longitud = request.GET.get("longitud")
	pulso = request.GET.get("pulso")
	valles = request.GET.get("valles")
	picos = request.GET.get("picos")
	estable = request.GET.get("estable")
	periodo = request.GET.get("periodo")

	#GUARDO EL PULSO
	p = Pulsos()
	p.device = Device.objects.get(codigo=id_dispo)
	p.lng = longitud
	p.lat = latitud
	p.BPM = pulso
	p.save()

	#GUARDO LA GRAFICA
	g = Grafica()
	g.pulso = p
	g.valles = valles
	g.picos = picos
	g.estable = estable
	g.periodo = periodo
	g.save()

	return HttpResponse("True")



@csrf_exempt
def get_lps(request):#Funcion para graficar el ultimo pulso :)
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
def get_lps2(request):#Funcion para graficar el GRAFICA PPG FOTOPLETISMOGRAMA
	try:
		id_dispo = request.POST.get("id_dispo")
		ult_pulso = Pulsos.objects.filter(device=Device.objects.get(codigo=id_dispo)).order_by('-id')[0]
		grafica = Grafica.objects.get(pulso=ult_pulso)
		result = dict(valles=grafica.valles,
					  picos = grafica.picos,
					  estable = grafica.estable,
					  periodo = grafica.periodo,
					  BPM = ult_pulso.BPM
					)
	except:
		result = dict(valles=0,
					  picos=0,
					  estable=0,
					  periodo=0,
					  BPM = 0
					  )

	return HttpResponse(json.dumps(result), content_type='application/json')


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


def reportexFecha(request, id_pac):
	pac = Paciente.objects.get(id=id_pac)
	today = datetime.now().date()
	tomorrow = today + timedelta(1)
	if (request.GET.get('datepiker') == None or request.GET.get('datepiker2') == None):
		# pulsos = Pulsos.objects.filter(device=pac.devide1.id)
		pulsos= Pulsos.objects.all()
	else:
		try:
			date1 = request.GET.get('datepiker')
			date2 = request.GET.get('datepiker2')

			# DATE
			start_date = datetime.strptime(date1, "%Y-%m-%d").date()
			end_date = datetime.strptime(date2, "%Y-%m-%d").date()

			#TIME
			#t1 = datetime.strptime("09:25:00", '%H:%M:%S').time()

			pulsos = Pulsos.objects.filter(device=pac.devide1.id, fecha__range=(start_date, end_date))
		except:
			pulsos = Pulsos.objects.all()

	return render(request, 'reportes_xfecha.html', locals())


def reportexPacienteyFecha(request):
	if(request.GET.get('datepiker') != None and request.GET.get('datepiker2') != None and request.GET.get('idpaciente') != None and request.GET.get('idpaciente') != '--------'):
		try:
			filtro = request.GET.get('idpaciente')
			pac1 = Paciente.objects.get(id=filtro)
			date1 = request.GET.get('datepiker')
			date2 = request.GET.get('datepiker2')
			# DATE
			start_date = datetime.strptime(date1, "%Y-%m-%d").date()
			end_date = datetime.strptime(date2, "%Y-%m-%d").date()
			pulsos = Pulsos.objects.filter(device=pac1.devide1.id, fecha__range=(start_date, end_date))
		except:
			messages.add_message(request, messages.ERROR, 'No ah seleccionado ningun paciente o ningun rango de fechas')
			msj_error = "No hay registro de pulsos en ese rango";
	pacientes = Paciente.objects.all()
	return render(request, 'reporte_xPaciente_Fecha.html', locals())


def modal(request):
	#DOCTOR
	#Tiene q detectar cualquier alerta de sus pacientes :O

	#PACIENTE

	return render(request, 'pruebaModal.html', locals())



