from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.ListaSolicitud.as_view(), name='lista'),
    path('nueva', views.NuevaSolicitud.as_view(), name='nueva'),
    path('editar/<str:pk>', views.EditarSolicitud.as_view(), name='editar'),
    path('detalle/<str:pk>', views.DetalleSolicitud.as_view(), name='detalle'),
]
