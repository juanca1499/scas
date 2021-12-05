from django.urls import path
from . import views

app_name = 'estudio_socioeconomico'

urlpatterns = [
    path('', views.ListaEstudio.as_view(), name='lista'),
    path('nuevo', views.NuevoEstudioSocioeconomico.as_view(), name='nuevo'),
    path('detalle/<str:pk>', views.DetalleEstudio.as_view(), name='detalle'),   
]