from django.urls import path
from . import views

app_name = 'estudio_socioeconomico'

urlpatterns = [
    path('', views.ListaEstudio.as_view(), name='lista'),
]