from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Solicitud
from usuarios.models import Usuario
from .forms import SolicitudForm


class ListaSolicitud(LoginRequiredMixin,ListView):
    model = Solicitud
    context_object_name = 'solicitudes'
    
    def get(self,request,*args,**kwargs):
        user = request.user
        if user.is_superuser == 1:
            return super().get(request,*args,**kwargs)
        # Se obtiene el usuario logueado
        usuario = get_object_or_404(Usuario,username=request.user.username)
        # Es capturista, se muestran solamente las solicitudes que el usuario ha registrado
        lista_solicitudes = Solicitud.objects.filter(usuario=usuario.id)
        # Se obtiene asigna el context_object_name definido 
        self.object_list = self.get_queryset()
        # Se agregan las solicitudes filtradas a la lista de variables a pasar al template
        context = self.get_context_data()
        context['solicitudes'] = lista_solicitudes
        return self.render_to_response(context)
    
class NuevaSolicitud(LoginRequiredMixin, CreateView):
    model = Solicitud
    form_class = SolicitudForm
    extra_context = {'etiqueta': 'Nueva', 'boton': 'Agregar'}
    success_url = reverse_lazy('solicitudes:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(NuevaSolicitud, self).form_invalid(form)
    
    def form_valid(self, form):
        self.solicitud = form.save(commit=False)
        usuario = get_object_or_404(Usuario,username=self.request.user.username)
        self.solicitud.usuario = usuario
        self.solicitud.save()
        messages.success(self.request, 'Solicitud guardada exitosamente.')
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
