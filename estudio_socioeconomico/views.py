from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import EstudioSocioeconomico

class ListaEstudio(ListView):
    model = EstudioSocioeconomico
    context_object_name = 'estudio'
    template_name = 'estudio_socioeconomico/estudio_list.html'
