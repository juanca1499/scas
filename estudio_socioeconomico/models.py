from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, FileExtensionValidator
from datetime import date

solo_numeros = RegexValidator(r'^[0-9]*$', 'Sólo se permiten números.')

validador_archivo = FileExtensionValidator(
    allowed_extensions = ['png','jpeg','jpg','pdf'],
    message = 'Sólo se permiten imágenes PNG, JPG, JPEG o PDF.'
)

class Escolaridad(models.Model):
    escolaridad = models.CharField("Grado de estudio", max_length=20)    
    
    def __str__(self):
        return self.escolaridad
    
    class Meta:
        verbose_name = 'Grado de estudio'
        verbose_name_plural = 'Grados de estudios'
    

class EstadoCivil(models.Model):
    estado_civil = models.CharField("Estado civil", max_length=20)    
    
    def __str__(self):
        return self.estado_civil
    
    class Meta:
        verbose_name = 'Estado civil'
        verbose_name_plural = 'Estados civiles'
    
class Discapacidad(models.Model):
    discapacidad = models.CharField("Discapacidad", max_length=20)    
    
    def __str__(self):
        return self.discapacidad
 
    class Meta:
        verbose_name = 'Discpacidad'
        verbose_name_plural = 'Discapacidades'
        
           
class Piso(models.Model):
    piso = models.CharField("Piso", max_length=20)    
    
    def __str__(self):
        return self.piso

    class Meta:
        verbose_name = 'Tipo de piso'
        verbose_name_plural = 'Tipos de piso'
    
class Techo(models.Model):
    techo = models.CharField("Techo", max_length=35)    
    
    def __str__(self):
        return self.techo
    
    class Meta:
        verbose_name = 'Tipo de techo'
        verbose_name_plural = 'Tipos de techo'
    
class Automovil(models.Model):
    automovil = models.CharField("Automóvil", max_length=35)    
    
    def __str__(self):
        return self.automovil
    
    class Meta:
        verbose_name = 'Automóvil'
        verbose_name_plural = 'Tipos de automóvil'
    
class TipoCombustible(models.Model):
    tipo_combustible = models.CharField("Tipo de combustible", max_length=35)    
    
    def __str__(self):
        return self.tipo_combustible
 
    class Meta:
        verbose_name = 'Tipo de combustible'
        verbose_name_plural = 'Tipos de combustible'
 
class Ocupacion(models.Model):
    ocupacion = models.CharField("Ocupación", max_length=35)    
    
    def __str__(self):
        return self.ocupacion 
    
    class Meta:
        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciones'
    
class CasaEs(models.Model):
    casa_es = models.CharField("Su casa es", max_length=35)    
    
    def __str__(self):
        return self.casa_es
    
    class Meta:
        verbose_name = 'Su casa es'
        verbose_name_plural = 'Su casa es'
    
class ServicioSalud(models.Model):
    servicio = models.CharField("Cuenta con servicio de", max_length=35)    
    
    def __str__(self):
        return self.servicio
    
    class Meta:
        verbose_name = 'Servicio de salud'
        verbose_name_plural = 'Servicios de salud'
    
class EstudioSocioeconomico(models.Model):
    folio = models.AutoField("Folio", primary_key=True)
    fecha_actual = models.DateField("Fecha")
    credencial = models.FileField("Credencial INE/IFE", upload_to='estudio/ine/', validators=[validador_archivo])
    comprobante_domicilio = models.FileField("Comprobante de domicilio", upload_to='estudio/comprobante/', validators=[validador_archivo])
    solicitud = models.ForeignKey("solicitudes.Solicitud", verbose_name="Solicitud", on_delete=models.CASCADE)
        
    @property
    def calcular_edad(solicitud):
        if solicitud.fecha_nacimiento:
            hoy = date.today()
            return hoy.year - solicitud.fecha_nacimiento.year - ((hoy.month, hoy.day) < (solicitud.fecha_nacimiento.month, solicitud.fecha_nacimiento.day))
        return 0  # cuando la fecha de nacimiento es 0
    
    
    calle = models.CharField('Calle', max_length=40)
    numero_interior = models.PositiveIntegerField(
        'Número interior', default=1,validators=[MinValueValidator(1)])
    numero_exterior = models.PositiveIntegerField(
        'Número exterior',blank=True,null=True ,validators=[MinValueValidator(1)])
    colonia = models.CharField("Colonia",max_length=35)
    codigo_postal = models.CharField(
        'Código Postal', max_length=5, validators=[MinLengthValidator(5), 
                                                   solo_numeros])
    localidad = models.ForeignKey("usuarios.Localidad",verbose_name='Localidad',on_delete=models.CASCADE)
    municipio = models.ForeignKey("usuarios.Municipio",verbose_name='Municipio',on_delete=models.CASCADE)
    estado = models.ForeignKey("usuarios.Estado",verbose_name='Estado',on_delete=models.CASCADE)
    entre_calles = models.CharField("Entre calle y calle", max_length=60, blank=True, null=True)
    
    telefono = models.CharField('Teléfono', max_length=10, validators=[
                                MinLengthValidator(10), solo_numeros])
    cabeza_familia = models.BooleanField("Es cabeza de familia", default=False)
    escolaridad = models.ForeignKey(Escolaridad, verbose_name="Escolaridad", on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion, verbose_name="Ocupacion", on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, verbose_name="Estado civil", on_delete=models.CASCADE)
    discapacidad = models.ForeignKey(Discapacidad, verbose_name="Discapacidad", on_delete=models.CASCADE)
    
    una_planta = models.BooleanField("1 Planta", default=False)
    dos_planta = models.BooleanField("2 Planta", default=False)
    tres_planta = models.BooleanField("3 Planta o más", default=False)
    sala_comedor = models.BooleanField("Sala/comedor", default=False)
    cocina = models.BooleanField("Cocina", default=False)
    patio = models.BooleanField("Patio", default=False)
    cochera = models.BooleanField("Cochera", default=False)
    numero_recamaras = models.IntegerField("Número de recamaras")    
    numero_banios = models.IntegerField("Número de baños")    
    otros_caracteristicas_casa = models.CharField("Otro", max_length=60,blank=True, null=True)
    
    piso_es =  models.ForeignKey(Piso, verbose_name="El piso es", on_delete=models.CASCADE)
    techo_es =  models.ForeignKey(Techo, verbose_name="El techo es", on_delete=models.CASCADE)
    automovil =  models.ForeignKey(Automovil, verbose_name="Automóvil", on_delete=models.CASCADE)
    tipo_combustible =  models.ForeignKey(TipoCombustible, verbose_name="Tipo de combustible", on_delete=models.CASCADE)
    
    casa_es = models.ForeignKey(CasaEs, verbose_name="Su casa es", on_delete=models.CASCADE)
    casa_energia = models.BooleanField("Energía Eléctrica", default=False)
    casa_drenaje = models.BooleanField("Drenaje", default=False)
    casa_potable = models.BooleanField("Agua Potable", default=False)
    casa_gas = models.BooleanField("Instalación Gas", default=False)
    casa_lavadora = models.BooleanField("Lavadora de ropa", default=False)
    casa_refrigerador = models.BooleanField("Refrigerador", default=False)
    casa_tv = models.BooleanField("T.V.", default=False)
    casa_tel_fijo = models.BooleanField("Teléfono fijo", default=False)
    casa_tel_celular = models.BooleanField("Teléfono celular", default=False)
    casa_microondas = models.BooleanField("Horno de microondas", default=False)
    casa_radio = models.BooleanField("Radio/Stéreo", default=False)
    casa_dvd = models.BooleanField("DVD", default=False)
    casa_computadora = models.BooleanField("Computadora", default=False)
    casa_laptop = models.BooleanField("Laptop", default=False)
    
    servicio_salud = models.ForeignKey(ServicioSalud, verbose_name="Servicio de salud", on_delete=models.CASCADE)
    enfermedad_cancer = models.BooleanField("Cáncer", default=False)
    enfermedad_quemaduras = models.BooleanField("Quemaduras", default=False)
    enfermedad_epilepsia = models.BooleanField("Epilepsia", default=False)
    enfermedad_hipertension = models.BooleanField("Hipertensión", default=False)
    enfermedad_presion_baja = models.BooleanField("Presión baja", default=False)
    enfermedad_discapacidad = models.BooleanField("Discapacidad", default=False)
    enfermedad_cardiacos = models.BooleanField("Cardíacos", default=False)
    enfermedad_estrabismo = models.BooleanField("Estrabismo", default=False)
    enfermedad_renales = models.BooleanField("Renales", default=False)
    enfermedad_alergia = models.BooleanField("Alergías", default=False)
    enfermedad_paladar_hendido = models.BooleanField("Paladar Hendido", default=False)
    enfermedad_cardiopatias = models.BooleanField("Cardiopatías", default=False)
    enfermedad_diabetes = models.BooleanField("Diabetes", default=False)
    enfermedad_alzhaimer = models.BooleanField("Alhzaimer", default=False)
    enfermedad_otro = models.CharField("Otro (Especifique)", max_length=60,blank=True, null=True)
    receta = models.FileField("Receta en caso de ser necesario", upload_to=' estudio/receta/', validators=[validador_archivo],blank=True,null=True)
       
    class Meta:
        verbose_name = 'Estudio socioesconomico'
        verbose_name_plural = 'Estudios socioeconomicos'
        
    def get_folio_formateado(self):
        return str(self.folio).zfill(4)