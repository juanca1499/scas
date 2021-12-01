from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Solicitud
from .forms import SolicitudForm


class ListaSolicitud(ListView):
    model = Solicitud


class NuevaSolicitud(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    success_url = reverse_lazy('solicitudes:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super().form_invalid(form)
