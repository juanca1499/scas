from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Usuario
from .forms import FormUsuario, FormUsuarioEditar


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
class UsuarioLogout(LoginRequiredMixin, LogoutView):
    template_name='login.html'
    
class UsuarioLista(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.view_usuario'
    model = Usuario
    context_object_name = 'usuarios'
    
class UsuarioNuevo(PermissionRequiredMixin, CreateView):
    permission_required = 'usuarios.add_usuario'
    model = Usuario
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    form_class = FormUsuario
    success_url = reverse_lazy('usuarios:lista')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(UsuarioNuevo, self).form_invalid(form)
    
@login_required
@permission_required('usuarios.delete_usuario', raise_exception=True)
def baja_usuario(request, pk):
    if request.method == "POST":
        usuario = get_object_or_404(Usuario, id=pk)
        usuario.dado_baja = True
        usuario.save()
        messages.success(request, '¡Cuenta dada de baja con éxito!')
    return redirect('usuarios:lista')

class UsuarioEditar(PermissionRequiredMixin, UpdateView):
    permission_required = 'usuarios.change_usuario'
    model = Usuario
    form_class = FormUsuarioEditar
    template_name = 'usuarios/usuario_form_editar.html'
    extra_context = {'etiqueta': 'Editar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay datos inválidos en el formulario.')
        return super(UsuarioEditar, self).form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, '¡Registro actualizado con éxito!')
        return super(UsuarioEditar, self).form_valid(form)
    
class UsuarioDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'usuarios.view_usuario'
    model = Usuario
    context_object_name = 'usuario'