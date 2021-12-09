from django import forms
from django.forms import widgets

from .models import Usuario


class DateInput(forms.DateInput):
    input_type = 'date'

class FormUsuario(forms.ModelForm):
    
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
    widget=DateInput(
        format='%Y-%m-%d',
        attrs={'class':'form-control','placeholder':'Fecha de nacimiento'}),
    required=True)

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'segundo_apellido', 'fecha_nacimiento', 'calle', 
                  'numero_interior', 'numero_exterior', 'colonia', 'codigo_postal', 'estado',
                  'municipio', 'localidad', 'email', 'telefono', 'ine', 'username', 'password')

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
