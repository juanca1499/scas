from django.contrib import admin

from .models import EstatusSolicitud, Solicitud

# Register your models here.
admin.site.register(EstatusSolicitud)
admin.site.register(Solicitud)
