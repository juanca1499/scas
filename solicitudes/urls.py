from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.ListaSolicitud.as_view(), name='lista'),
    path('nueva', views.NuevaSolicitud.as_view(), name='nueva'),
]
