from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from estudio_socioeconomico.test.test_views import TestViews
from django.core.files.uploadedfile import SimpleUploadedFile

from estudio_socioeconomico.models import *
from estudio_socioeconomico.forms import EstudiosocioeconomicoForm

class TestForms(TestCase):
    def setUp(self):
        test_view = TestViews()
        
        self.estudio = {
            'fecha_actual':'2021-11-17',
            'solicitud': test_view.agrega_solicitud(test_view.agrega_usuario()),
            'edad': 20,
            'telefono': '4921736547',
            'cabeza_familia': True,
            'ocupacion': test_view.agrega_ocupacion(),
            'escolaridad': test_view.agrega_escolaridad(),
            'estado_civil': test_view.agrega_estado_civil(),
            'discapacidad': test_view.agrega_discapacidad(),          
            'automovil': test_view.agrega_automovil(),
            'tipo_combustible': test_view.agrega_tipo_combustible(),  
            'calle': 'Adelitas revolucionarias',
            'numero_exterior': 9,
            'colonia': 'Adelitas',
            'codigo_postal': '98613',
            'estado': test_view.agrega_estado(),
            'municipio': test_view.agrega_municipio(),
            'localidad': test_view.agrega_localidad(),
            'tres_planta': True,
            'sala_comedor':True ,
            'cocina': True,
            'numero_recamaras': 1,
            'numero_banios': 2,
            'piso_es': test_view.agrega_piso(),
            'techo_es': test_view.agrega_techo(),
            'casa_es': test_view.agrega_casa(),
            'casa_energia': True,
            'casa_drenaje': True,
            'servicio_salud': test_view.agrega_servicio_salud(),
            'enfermedad_cancer': True,
            'enfermedad_quemaduras': True,
            'enfermedad_epilepsia': True
        }
        self.archivos = {
            'credencial': SimpleUploadedFile('media/testfiles/ine.png', b'123456'),
            'comprobante_domicilio': SimpleUploadedFile('media/testfiles/comprobante.png', b'123456'),
        }
        
    def test_estudio_valido(self):
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())
          
    def test_estudio_credencial_requerida(self):
        self.archivos['credencial'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_comprobante_domicilio_requerido(self):
        self.archivos['comprobante_domicilio'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_solicitud_vacia(self):
        self.estudio['solicitud'] = None
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())

    def test_estudio_escolaridad_requerido(self):
        self.estudio['escolaridad'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_edad_vacio(self):
        self.estudio['edad'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())
    
    def test_estudio_calle_requerido(self):
        self.estudio['calle'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_numero_exterior_requerido(self):
        self.estudio['numero_exterior'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())

    def test_estudio_numero_interior_vacio(self):
        self.estudio['numero_interior'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())

    def test_estudio_colonia_requerida(self):
        self.estudio['colonia'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_codigo_postal_requerida(self):
        self.estudio['codigo_postal'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_estado_requerido(self):
        self.estudio['estado'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_municipio_requerido(self):
        self.estudio['municipio'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_localidad_requerido(self):
        self.estudio['localidad'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_entre_calles_vacio(self):
        self.estudio['entre_calles'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertTrue(form.is_valid())
        
    def test_estudio_telefono_requerido(self):
        self.estudio['telefono'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
               
    def test_estudio_escolaridad_requerido(self):
        self.estudio['escolaridad'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_ocupacion_requerido(self):
        self.estudio['ocupacion'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_estado_civil_requerido(self):
        self.estudio['estado_civil'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_discapacidad_requerido(self):
        self.estudio['discapacidad'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
                
        
    def test_estudio_numero_recamaras_requerido(self):
        self.estudio['numero_recamaras'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_numero_banios_requerido(self):
        self.estudio['numero_banios'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
                
    def test_estudio_piso_es_requerido(self):
        self.estudio['piso_es'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_techo_es_requerido(self):
        self.estudio['techo_es'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_automovil_requerido(self):
        self.estudio['automovil'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_tipo_combustible_requerido(self):
        self.estudio['tipo_combustible'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_casa_es_requerido(self):
        self.estudio['casa_es'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
               
    def test_estudio_servicio_salud_requerido(self):
        self.estudio['servicio_salud'] = ''
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
            
    def test_estudio_fecha_formato(self):
        self.estudio['fecha_actual'] = '2 de diciembre de 1999'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
       
    def test_estudio_fecha_formato_eu(self):
        self.estudio['fecha_actual'] = '09/29/2021'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid()) 

    def test_estudio_credencial_extension(self):
        self.archivos['credencial'] = 'imagen.docx'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid()) 
    
    def test_estudio_comprobante_extension(self):
        self.archivos['comprobante_domicilio'] = 'imagen.docx'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid()) 
    
    def test_estudio_receta_extension(self):
        self.archivos['receta'] = 'imagen.docx'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid()) 
        
    def test_estudio_calle_longitud_excedida(self):
        self.estudio['calle'] = 'Real de angelesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_numero_exterior_negativo(self):
        self.estudio['numero_exterior'] = -34
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_numero_interior_negativo(self):
        self.estudio['numero_interior'] = -34
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
    
    def test_estudio_edad_negativo(self):
        self.estudio['edad'] = -34
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
    
    def test_estudio_colonia_longitud_excedida(self):
        self.estudio['colonia'] = 'Real de angelesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_codigo_postal_longitud_excedida(self):
        self.estudio['codigo_postal'] = 8348312121323
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_codigo_postal_longitud_menor(self):
        self.estudio['codigo_postal'] = 8348
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_codigo_postal_solo_numeros(self):
        self.estudio['codigo_postal'] = 'doscientesochentassd'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_entre_calles_longitud_excedida(self):
        self.estudio['entre_calles'] = 'Real de angelesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_telefono_longitud_excedida(self):
        self.estudio['telefono'] = 8348312121323
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_telefono_longitud_menor(self):
        self.estudio['telefono'] = 8348
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_telefono_solo_numeros(self):
        self.estudio['telefono'] = 'doscientesochentassd'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_numero_recamaras_solo_numeros(self):
        self.estudio['numero_recamaras'] = 'doscientesochentassd'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
    
    def test_estudio_numero_recamaras_negativos(self):
        self.estudio['numero_recamaras'] = -34
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_estudio_otros_caracteristicas_casa_longitud_excedida(self):
        self.estudio['otros_caracteristicas_casa'] = 'Real de angelesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

    def test_estudio_enfermedad_otro_longitud_excedida(self):
        self.estudio['enfermedad_otro'] = 'Real de angelesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = EstudiosocioeconomicoForm(self.estudio,files=self.archivos)
        self.assertFalse(form.is_valid())

        
    
        
    
        
    