from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Solicitud
from .forms import SolicitudForm


class ListaSolicitud(ListView):
    model = Solicitud
    context_object_name = 'solicitudes'
    
    
class NuevaSolicitud(LoginRequiredMixin, CreateView):
    model = Solicitud
    form_class = SolicitudForm
    extra_context = {'etiqueta': 'Nueva', 'boton': 'Agregar'}
    success_url = reverse_lazy('solicitudes:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(NuevaSolicitud, self).form_invalid(form)
    
    def form_valid(self, form):
        messages.error(self.request, 'Solicitud guardada exitosamente.')
        return super(NuevaSolicitud, self).form_valid(form)
    
    
class EditarSolicitud(LoginRequiredMixin, UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('solicitudes:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Solicitud actualizada')
        return super(EditarSolicitud, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario')
        return super(EditarSolicitud, self).form_invalid(form)
    
class DetalleSolicitud(LoginRequiredMixin, DetailView):
    model = Solicitud
    context_object_name = "solicitud"
