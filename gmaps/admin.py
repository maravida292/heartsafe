from django.contrib import admin
from .models import *


class PulsosAdmin(admin.ModelAdmin):
	list_display = ('id','device', 'lat', 'lng')
	list_filter = ('fecha','device',)


class DeviceAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'codigo')
	list_filter = ('marca','ocupado',)


admin.site.register(Pulsos, PulsosAdmin)
admin.site.register(Device,DeviceAdmin)
