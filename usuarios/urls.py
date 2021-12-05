from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/',views.UsuarioLogout.as_view(), name='logout'),
    path('lista/', views.UsuarioLista.as_view(), name='lista'),
]
