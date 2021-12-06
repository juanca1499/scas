# from django.test import TestCase
# from django.contrib.auth.forms import AuthenticationForm
# from estudio_socioeconomico.test.test_views import TestViews
# from django.core.files.uploadedfile import SimpleUploadedFile

# from estudio_socioeconomico.models import *
# from estudio_socioeconomico.forms import EstudiosocioeconomicoForm

# class TestForms(TestCase):
#     def setUp(self):
#         test_view = TestViews()
        
#         self.estudio = {
#             'fecha_actual':'2021-11-17',
#             'escolaridad': test_view.agrega_escolaridad(),
#             'edad': 20,
#             'calle': 'Adelitas revolucionarias',
#             'numero_exterior': 9,
#             'colonia': 'Adelitas',
#             'codigo_postal': 98613,
#             'estado': test_view.agrega_estado(),
#             'municipio': test_view.agrega_municipio(),
#             'localidad': test_view.agrega_localidad(),
#             'telefono': '4921736547',
#             'cabeza_familia': True,
#             'estado_civil': test_view.agrega_estado_civil(),
#             'discapacidad': test_view.agrega_discapacidad(),
#             'tres_planta': True,
#             'sala_comedor':True ,
#             'cocina': True,
#             'numero_recamaras': 1,
#             'numero_banios': 2,
#             'piso_es': test_view.agrega_piso(),
#             'techo_es': test_view.agrega_techo(),
#             'automovil': test_view.agrega_automovil(),
#             'tipo_combustible': test_view.agrega_tipo_combustible(),
#             'casa_es': test_view.agrega_casa(),
#             'casa_energia': True,
#             'casa_drenaje': True,
#             'ocupacion': test_view.agrega_ocupacion(),
#             'servicio_salud': test_view.agrega_servicio_salud(),
#             'enfermedad_cancer': True,
#             'enfermedad_quemaduras': True,
#             'enfermedad_epilepsia': True
#         }
#         self.archivos = {
#             'credencial': SimpleUploadedFile('media/testfiles/ine.png', b'123456'),
#             'comprobante_domicilio': SimpleUploadedFile('media/testfiles/comprobante.png', b'123456'),
#         }