from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MaxValueValidator, RegexValidator, MinLengthValidator, MinValueValidator, FileExtensionValidator


class Estado(models.Model):
    nombre = models.CharField('Estado', max_length=35)
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField('Municipio', max_length=35)
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Localidad(models.Model):
    nombre = models.CharField('Localidad', max_length=40)
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

solo_numeros = RegexValidator(r'^[0-9]*$', 'Sólo se permiten números.')
validador_archivo = FileExtensionValidator(
    allowed_extensions = ['png','jpeg','jpg','pdf'],
    message = 'Sólo se permiten imágenes PNG, JPG, JPEG o PDF.'
)

class Usuario(User):
    segundo_apellido = models.CharField('Segundo apellido', max_length=35, null=True, blank=True)
    calle = models.CharField('Calle', max_length=40)
    numero = models.IntegerField('Número', validators=[MinValueValidator(1,'El número debe estar entre 1 y 9999.'), MaxValueValidator(9999, 'El número debe estar entre 1 y 9999.')])
    colonia = models.CharField('Colonia', max_length=35)
    codigo_postal = models.CharField('Código postal', max_length=5, validators=[MinLengthValidator(5,'El código postal debe contener cinco dígitos.'),solo_numeros])
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, verbose_name='Localidad', on_delete=models.CASCADE)
    telefono = models.CharField('Teléfono', max_length=10, validators=[solo_numeros,MinLengthValidator(10, 'El teléfono debe contener diez dígitos.')])
    ine = models.FileField(upload_to='usuarios/ine/', max_length=100, validators=[validador_archivo])
    dado_baja = models.BooleanField('Dado de baja', default=False, validators=[MaxLengthValidator(1,'El campo sólo puede contener un dígito'),MinValueValidator(0,'Sólo se permiten los valores 0 y 1'),MaxValueValidator(1,'Sólo se permiten los valores 0 y 1')])