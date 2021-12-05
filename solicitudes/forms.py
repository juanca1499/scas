from django import forms
from .models import Solicitud


class DateInput(forms.DateInput):
    input_type = 'date'


class SolicitudForm(forms.ModelForm):
    fecha = forms.DateField(label='Fecha',
                            widget=DateInput(
                                format='%dd-%mm-%Y',
                                attrs={'class': 'form-control'}),
                            required=False)

    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
                                       widget=DateInput(
                                           format='%dd-%mm-%Y',
                                           attrs={'class': 'form-control'}),
                                       required=False)
    
    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].required = False

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
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'municipio':forms.Select(attrs={'class':'form-control', 'placeholder':'Municipio'}),
            'localidad':forms.Select(attrs={'class':'form-control', 'placeholder':'Localidad'}),
            'estatus':forms.Select(attrs={'class':'form-control', 'placeholder':'Estatus'}),
            'usuario':forms.HiddenInput(attrs={'class':'form-control'})
        }
