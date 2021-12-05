from django.contrib import admin

from .models import Estado, Municipio, Localidad

# Register your models here.
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Localidad)
