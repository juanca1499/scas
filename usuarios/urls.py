from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/',views.UsuarioLogout.as_view(), name='logout'),
    path('usuarios/', views.UsuarioLista.as_view(), name='lista'),
    path('usuarios/nuevo', views.UsuarioNuevo.as_view(), name='nuevo'),
    path('usuarios/baja/<int:pk>', views.baja_usuario, name='baja'),
    path('usuarios/editar/<int:pk>', views.UsuarioEditar.as_view(), name='editar'),
    path('usuarios/detalle/<int:pk>', views.UsuarioDetalle.as_view(), name='detalle')
]
