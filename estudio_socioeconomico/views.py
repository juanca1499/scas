from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from solicitudes.models import Solicitud

from .models import EstudioSocioeconomico
from .forms import EstudiosocioeconomicoForm

class ListaEstudio(ListView):
    model = EstudioSocioeconomico
    context_object_name = 'estudio'
    template_name = 'estudio_socioeconomico/estudio_list.html'

class NuevoEstudioSocioeconomico(LoginRequiredMixin, CreateView):
    model = EstudioSocioeconomico
    form_class = EstudiosocioeconomicoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    template_name = 'estudio_socioeconomico/estudio_form.html'
    success_url = reverse_lazy('estudio_socioeconomico:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(NuevoEstudioSocioeconomico, self).form_invalid(form)
    
    def form_valid(self, form):
        self.estudio_socioeconomico = form.save(commit=False)
        # solicitud_nombre = get_object_or_404(Solicitud,nombre=self.request.solicitud.nombre)
        # print()
        # self.estudio_socioeconomico.nombre = solicitud_nombre
        self.estudio_socioeconomico.save()
        messages.success(self.request, 'Solicitud guardada exitosamente.')
        return super(NuevoEstudioSocioeconomico, self).form_valid(form)
    
class DetalleEstudio(LoginRequiredMixin, DetailView):
    model = EstudioSocioeconomico
    context_object_name = "estudio"
    template_name = 'estudio_socioeconomico/estudio_detail.html'