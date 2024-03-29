from django import forms
from .models import Solicitud


class DateInput(forms.DateInput):
    input_type = 'date'


class SolicitudForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
                                       widget=DateInput(
                                           format='%Y-%m-%d',
                                           attrs={'class': 'form-control'}),
                                       required=False)

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].required = False
        self.fields['fecha'].required = False

    class Meta:
        model = Solicitud
        fields = '__all__'

        widgets = {
            'fecha': forms.HiddenInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.NumberInput(attrs={'class': 'form-control'}),
            'seccion': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado'}),
            'municipio': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Municipio'}),
            'localidad': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Localidad'}),
            'estatus': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estatus'}),
            'usuario': forms.HiddenInput(attrs={'class': 'form-control'})
        }
