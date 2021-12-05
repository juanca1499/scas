from django import forms
from django.forms import widgets 

from .models import Usuario

class FormUsuario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','segundo_apellido','calle','numero','colonia','codigo_postal','estado','municipio','localidad','email','telefono','ine','username','password',)
        
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primer apellido'}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Segundo apellido'}),
            'calle':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Calle'}),
            'numero':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Número'}),
            'colonia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Colonia'}),
            'codigo_postal':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Código postal'}),
            'estado':forms.Select(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'municipio':forms.Select(attrs={'class':'form-control', 'placeholder':'Municipio'}),
            'localidad':forms.Select(attrs={'class':'form-control', 'placeholder':'Localidad'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}),
            'ine':forms.FileInput(attrs={'class':'form-control', 'placeholder':'INE'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Contraseña'}),
        }