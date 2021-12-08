from django.shortcuts import get_object_or_404
from django.urls.base import resolve
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from solicitudes.models import Solicitud
from usuarios.models import Usuario

from .models import EstudioSocioeconomico
from .forms import EstudiosocioeconomicoForm

class ListaEstudio(ListView):
    model = EstudioSocioeconomico
    context_object_name = 'estudios'
    template_name = 'estudio_socioeconomico/estudio_list.html'
    
    # def get(self,request,*args,**kwargs):
    #     user = request.user
    #     if user.is_superuser == 1:
    #         return super().get(request,*args,**kwargs)
    #     # Se obtiene el usuario logueado
    #     usuario = get_object_or_404(Usuario,username=request.user.username)
    #     # Es capturista, se muestran solamente las solicitudes que el usuario ha registrado
    #     lista_solicitudes = Solicitud.objects.filter(usuario=usuario.id)
    #     # Se obtiene asigna el context_object_name definido 
    #     self.object_list = self.get_queryset()
    #     # Se agregan las solicitudes filtradas a la lista de variables a pasar al template
    #     context = self.get_context_data()
    #     context['solicitudes'] = lista_solicitudes
    #     return self.render_to_response(context)

class NuevoEstudioSocioeconomico(LoginRequiredMixin, CreateView):
    model = EstudioSocioeconomico
    form_class = EstudiosocioeconomicoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    template_name = 'estudio_socioeconomico/estudio_form.html'
    success_url = reverse_lazy('estudio_socioeconomico:lista')
           
    def dispatch(self, request, *args, **kwargs):
        self.solicitud = get_object_or_404(Solicitud, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.solicitud = self.solicitud
        self.estudio_socioeconomico = form.save(commit=False)
        self.estudio_socioeconomico.save()
        messages.success(self.request, 'Estudio socioeconómico guardado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(NuevoEstudioSocioeconomico, self).form_invalid(form)
    
class DetalleEstudio(LoginRequiredMixin, DetailView):
    model = EstudioSocioeconomico
    context_object_name = "estudio"
    template_name = 'estudio_socioeconomico/estudio_detail.html'
    
class EditarEstudio(LoginRequiredMixin, UpdateView):
    model = EstudioSocioeconomico
    form_class = EstudiosocioeconomicoForm
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('estudio_socioeconomico:lista')
    template_name = 'estudio_socioeconomico/estudio_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Estudio socioeconómico actualizado')
        return super(EditarEstudio, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario')
        return super(EditarEstudio, self).form_invalid(form)