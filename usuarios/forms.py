from django import forms
from django.contrib.auth.models import Group

from .models import Usuario


class DateInput(forms.DateInput):
    input_type = 'date'

class FormUsuario(forms.ModelForm):
    
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
    widget=DateInput(
        format='%Y-%m-%d',
        attrs={'class':'form-control','placeholder':'Fecha de nacimiento'}),
    required=True)
    
    tipo_usuario = forms.ChoiceField(label='Tipo de usuario',
    choices=[('','---------'),('1','Administrador'),('2','Encuestador')],
    widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Tipo de usuario'}),
    required=True)
                
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'segundo_apellido', 'fecha_nacimiento', 'calle', 
                  'numero_interior', 'numero_exterior', 'colonia', 'codigo_postal', 'estado',
                  'municipio', 'localidad', 'email', 'telefono', 'ine', 'username', 'password',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'}),
            'numero_interior': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número interior'}),
            'numero_exterior': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número interior'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código postal'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'municipio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Municipio'}),
            'localidad': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Localidad'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'ine': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }

    def save(self, commit=True):
        user = super(FormUsuario, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class FormUsuarioEditar(forms.ModelForm):

    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
    widget=DateInput(
        format='%Y-%m-%d',
        attrs={'class':'form-control','placeholder':'Fecha de nacimiento'}),
    required=True)
    
    tipo_usuario = forms.ChoiceField(label='Tipo de usuario',
    choices=[('','---------'),('1','Administrador'),('2','Encuestador')],
    widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Tipo de usuario'}),
    required=True)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if self.instance.pk:
            if self.instance.is_superuser == 1:
                # Se selecciona por default la opción de Administrador.
                self.fields['tipo_usuario'].initial = '1'
            else: 
                # Se selecciona por default la opción de Encuestador.
                self.fields['tipo_usuario'].initial = '2'
            
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'segundo_apellido', 'fecha_nacimiento', 'calle', 
                  'numero_interior', 'numero_exterior', 'colonia', 'codigo_postal', 'estado',
                  'municipio', 'localidad', 'email', 'telefono', 'ine',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'}),
            'numero_interior': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número interior'}),
            'numero_exterior': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número interior'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código postal'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'municipio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Municipio'}),
            'localidad': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Localidad'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'ine': forms.FileInput(attrs={'class': 'form-control'}),
        }
