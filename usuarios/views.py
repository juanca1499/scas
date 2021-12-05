from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView, DetailView

from .models import Usuario


# Función correspondiente al login de los usuarios.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
    
        if usuario is not None:
            if usuario.is_active:
                auth_login(request, usuario)
                return redirect('solicitudes:lista')
        else:
            messages.error(request,'El usuario o la contraseña no son correctos')
            return redirect('usuarios:login')
    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Clase correspondiente al logout de los usuarios.
class UsuarioLogout(LogoutView):
    template_name='login.html'
    
class UsuarioLista(ListView):
    model = Usuario
    context_object_name = 'usuarios'
