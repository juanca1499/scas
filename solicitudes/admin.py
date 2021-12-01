from django.contrib import admin

from .models import EstadoCivil, GradoEstudios, Ocupacion

# Register your models here.
admin.site.register(EstadoCivil)
admin.site.register(GradoEstudios)
admin.site.register(Ocupacion)
