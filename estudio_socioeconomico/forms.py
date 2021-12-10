from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class EstudiosocioeconomicoForm(forms.ModelForm):
    fecha_actual = forms.DateField(label='Fecha',
                                   widget=DateInput(
                                       format='%Y-%m-%d',
                                       attrs={'class': 'form-control'}),
                                   required=False)

    class Meta:
        model = EstudioSocioeconomico
        exclude = ['solicitud','folio','edad']

        widgets = {
            'credencial': forms.FileInput(attrs={'class': 'form-control'}),
            'comprobante_domicilio': forms.FileInput(attrs={'class': 'form-control'}),
            'escolaridad': forms.Select(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_interior': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_exterior': forms.NumberInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'entre_calles': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cabeza_familia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'discapacidad': forms.Select(attrs={'class': 'form-control'}),
            'una_planta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dos_planta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tres_planta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sala_comedor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cocina': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'patio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cochera': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'numero_recamaras': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_banios': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros_caracteristicas_casa': forms.TextInput(attrs={'class': 'form-control'}),
            'piso_es': forms.Select(attrs={'class': 'form-control'}),
            'techo_es': forms.Select(attrs={'class': 'form-control'}),
            'automovil': forms.Select(attrs={'class': 'form-control'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-control'}),
            'casa_es': forms.Select(attrs={'class': 'form-control'}),
            'casa_energia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_drenaje': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_potable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_gas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_lavadora': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_refrigerador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_tv': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_tel_fijo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_tel_celular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_microondas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_radio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_dvd ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_computadora': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casa_laptop ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ocupacion': forms.Select(attrs={'class': 'form-control'}),
            'servicio_salud': forms.Select(attrs={'class': 'form-control'}),
            'enfermedad_cancer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_quemaduras': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_epilepsia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_hipertension': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_presion_baja': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_discapacidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_cardiacos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_estrabismo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_renales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_alergia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_paladar_hendido': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_cardiopatias': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_diabetes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_alzhaimer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enfermedad_otro': forms.TextInput(attrs={'class': 'form-control'}),
            'receta': forms.FileInput(attrs={'class': 'form-control'})

        }
