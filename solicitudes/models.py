from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator

from usuarios.models import Usuario


solo_letras = RegexValidator(
    r'^[a-zA-Z\s\u00C0-\u00FF]*$', 'Sólo se permiten letras.')
solo_numeros = RegexValidator(r'^[0-9]*$', 'Sólo se permiten números.')
curp = RegexValidator(r'^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$')
no_numeros = RegexValidator(r'[^0-9]')


class Solicitud(models.Model):
    fecha = models.DateField()
    nombre = models.CharField('Nombre', max_length=45,
                              validators=[solo_letras])
    primer_apellido = models.CharField(
        'Primer Apellido', max_length=35, validators=[solo_letras])
    segundo_apellido = models.CharField(
        'Segundo apellido', max_length=35, blank=True, null=True, validators=[solo_letras])
    calle = models.CharField('Calle', max_length=34)
    numero = models.PositiveIntegerField(
        'Número', validators=[MinValueValidator(1)])
    codigo_postal = models.CharField(
        'Código Postal', max_length=5, validators=[MinLengthValidator(5), 
                                                   solo_numeros])
    seccion = models.CharField('Sección', max_length=4, validators=[
                               MinLengthValidator(4), solo_numeros])
    telefono = models.CharField('Teléfono', max_length=10, validators=[
                                MinLengthValidator(10), solo_numeros])
    curp = models.CharField('CURP', max_length=18, validators=[curp])
    #localidad = models.ForeignKey("usuarios.Localidad",verbose_name='Localidad',on_delete=models.CASCADE)
    #municipio = models.ForeignKey("usuarios.Municipio",verbose_name='Municipio',on_delete=models.CASCADE)
    #estado = models.ForeignKey("usuarios.Estado",verbose_name='Estado',on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField('Correo', max_length=50, blank=True, null=True)
    resumen = models.TextField('Resumen de la solicitud', blank=True, null=True)
    estatus = models.ForeignKey('solicitudes.EstatusSolicitud', related_name='Estatus de la solicitud', on_delete=models.CASCADE)
    #usuario = models.ForeignKey("usuarios.Usuario",verbose_name='Usuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        
        
class EstatusSolicitud(models.Model):
    estatus = models.CharField("Estatus de la solicitud", max_length=20)

    def __str__(self):
        return self.estado