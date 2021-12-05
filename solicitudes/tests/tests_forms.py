from django.test import TestCase
from django.contrib.auth.models import User
from solicitudes.tests.tests_views import TestViews
from solicitudes.forms import SolicitudForm
from solicitudes.models import Solicitud, EstatusSolicitud
from usuarios.models import Usuario


class TestForms(TestCase):
    def setUp(self):
        test_view = TestViews()
        
        self.usuario = {
            'first_name' : 'Juan Carlos',
            'last_name' : 'García',
            'calle' : 'Rafael Acuña',
            'numero' : 9,
            'colonia' : 'Artesanos',
            'codigo_postal' : 99343,
            'estado' : estado,
            'municipio' : municipio,
            'localidad' : localidad,
            'email' : 'garciamjuancarlos14@gmail.com',
            'telefono' : '4949428829',
            'ine' : None,
            'username' : 'juca',
            'password' : 'juca123'
        }
    
    def test_solicitud_form_valido(self):
        form = SolicitudForm(self.solicitud)
        self.assertTrue(form.is_valid())
        
    def test_solicitud_form_usuario_vacio(self):
        self.solicitud['usuario'] = None
        form = SolicitudForm(self.solicitud)
        self.assertTrue(form.is_valid())

    def test_solicitud_form_nombre_vacio(self):
        self.solicitud['nombre'] = ''
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_solicitud_form_segundo_apellido_permite_vacio(self):
        self.solicitud['segundo_apellido'] = ''
        form = SolicitudForm(self.solicitud)
        self.assertTrue(form.is_valid())

    def test_solicitud_form_curp_invalida(self):
        self.solicitud['curp'] = 'DICC12HZ'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_nombre_longitud_sobrepasada(self):
        self.solicitud['nombre'] = 'Gabriellllllllllllllllllllllllllllllllllllllll'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_nombre_con_numeros(self):
        self.solicitud['nombre'] = 'Gabriel 12'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_primer_apellido_longitud_minima(self):
        self.solicitud['primer_apellido'] = 'D'
        form = SolicitudForm(self.solicitud)
        self.assertTrue(form.is_valid())

    def test_primer_apellido_longitud_sobrepasada(self):
        self.solicitud['primer_apellido'] = 'Díazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_primer_apellido_con_numeros(self):
        self.solicitud['primer_apellido'] = 'Díaz123'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_segundo_apellido_con_numeros(self):
        self.solicitud['segundo_apellido'] = 'Curiel1999'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
        
    def test_segundo_apellido_longitud_sobrepasada(self):
        self.solicitud['segundo_apellido'] = 'Curiellllllllllllllllllllllllllllllll'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_calle_longitud_sobrepasada(self):
        self.solicitud['calle'] = 'Montes de ocaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_numero_con_letras(self):
        self.solicitud['numero'] = 'nueve'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_numero_en_cero(self):
        self.solicitud['numero'] = 0
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_longitud_cuatro(self):
        self.solicitud['codigo_postal'] = '9861'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_longitud_seis(self):
        self.solicitud['codigo_postal'] = '986134'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_con_letras(self):
        self.solicitud['codigo_postal'] = '9861t'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())        
        
    def test_seccion_longitud_tres(self):
        self.solicitud['seccion'] = '006'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_seccion_longitud_cinco(self):
        self.solicitud['seccion'] = '00643'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_seccion_con_letras(self):
        self.solicitud['seccion'] = '006a'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_telefono_nueve_digitos(self):
        self.solicitud['telefono'] = '494102515'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_telefono_once_digitos(self):
        self.solicitud['telefono'] = '49410251534'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_telefono_con_letras(self):
        self.solicitud['telefono'] = '494102515a'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())

    def test_correo_sin_arroba(self):
        self.solicitud['correo'] = 'gabriel_prueba_gmail.com'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())
        
    def test_correo_longitud_sobrepasada(self):
        self.solicitud['correo'] = 'gabriel_pruebaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com'
        form = SolicitudForm(self.solicitud)
        self.assertFalse(form.is_valid())