from django.contrib.auth.models import Group, Permission
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import datetime

from .models import Solicitud
from usuarios.models import Usuario, Estado, Municipio, Localidad
from estudio_socioeconomico.models import EstudioSocioeconomico
from .forms import SolicitudForm


class ListaSolicitud(PermissionRequiredMixin, ListView):
    permission_required = 'solicitudes.view_solicitud'
    model = Solicitud
    context_object_name = 'solicitudes'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser == 1:
            return super().get(request, *args, **kwargs)
        # Se obtiene el usuario logueado
        usuario = get_object_or_404(Usuario, username=request.user.username)
        # Es capturista, se muestran solamente las solicitudes que el usuario ha registrado
        lista_solicitudes = Solicitud.objects.filter(usuario=usuario.id)
        # Se obtiene asigna el context_object_name definido
        self.object_list = self.get_queryset()
        # Se agregan las solicitudes filtradas a la lista de variables a pasar al template
        context = self.get_context_data()
        context['solicitudes'] = lista_solicitudes
        return self.render_to_response(context)


class NuevaSolicitud(PermissionRequiredMixin, CreateView):
    permission_required = 'solicitudes.add_solicitud'
    model = Solicitud
    form_class = SolicitudForm
    extra_context = {'etiqueta': 'Nueva', 'boton': 'Registrar'}
    success_url = reverse_lazy('solicitudes:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario')
        return super(NuevaSolicitud, self).form_invalid(form)

    def form_valid(self, form):
        self.solicitud = form.save(commit=False)
        self.solicitud.fecha = datetime.datetime.now().strftime ("%Y-%m-%d")
        usuario = get_object_or_404(
            Usuario, username=self.request.user.username)
        self.solicitud.usuario = usuario
        self.solicitud.save()
        messages.success(self.request, 'Solicitud guardada exitosamente')
        return super(NuevaSolicitud, self).form_valid(form)


class EditarSolicitud(PermissionRequiredMixin, UpdateView):
    permission_required = 'solicitudes.edit_solicitud'
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


class DetalleSolicitud(PermissionRequiredMixin, DetailView):
    permission_required = 'solicitudes.view_solicitud'
    model = Solicitud
    context_object_name = "solicitud"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            estudio = EstudioSocioeconomico.objects.get(
                solicitud=self.object.id)
        except EstudioSocioeconomico.DoesNotExist:
            estudio = None

        if estudio != None:
            context['estudio'] = True
            context['estudio_folio'] = estudio.folio
        else:
            context['estudio'] = False

        return context


def obtiene_municipios(request):
    # estado = get_object_or_404(Estado, id=id_estado)
    if request.method == 'GET':
        return JsonResponse({'error': 'Petición incorrecta'}, safe=False,  status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error': 'No se encontrar municipios para ese estado'})
    else:
        json.append({'id': -1, 'nombre': '---------'})

    for municipio in municipios:
        json.append({'id': municipio.id, 'nombre': municipio.nombre})
    return JsonResponse(json, safe=False)


def obtiene_localidades(request):
    # estado = get_object_or_404(Estado, id=id_estado)
    if request.method == 'GET':
        return JsonResponse({'error': 'Petición incorrecta'}, safe=False,  status=403)
    id_municipio = request.POST.get('id')
    localidades = Localidad.objects.filter(municipio_id=id_municipio)
    json = []
    if not localidades:
        json.append(
            {'error': 'No se encontrar localidades para ese municipio'})
    else:
        json.append({'id': -1, 'nombre': '---------'})

    for localidad in localidades:
        json.append({'id': localidad.id, 'nombre': localidad.nombre})
    return JsonResponse(json, safe=False)
