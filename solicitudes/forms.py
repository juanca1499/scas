from django import forms
from .models import Solicitud


class DateInput(forms.DateInput):
    input_type = 'date'


class SolicitudForm(forms.ModelForm):
    fecha = forms.DateField(label='Fecha',
                            widget=DateInput(
                                format='%Y-%m-%d',
                                attrs={'class': 'form-control'}),
                            required=False)

    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
                                       widget=DateInput(
                                           format='%Y-%m-%d',
                                           attrs={'class': 'form-control'}),
                                       required=False)

    class Meta:
        model = Solicitud
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.NumberInput(attrs={'class': 'form-control'}),
            'seccion': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'ultimo_grado_estudios': forms.Select(attrs={'class': 'form-control'}),
            'ocupacion': forms.Select(attrs={'class': 'form-control'}),
            'otra_ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
        }
