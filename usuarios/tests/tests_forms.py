from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from solicitudes.tests.tests_views import TestViews
from django.core.files.uploadedfile import SimpleUploadedFile

from usuarios.models import Usuario, Estado, Municipio, Localidad
from usuarios.forms import FormUsuario

class TestForms(TestCase):
    def setUp(self):
        test_view = TestViews()
        
        self.usuario = {
            'first_name' : 'Juan Carlos',
            'last_name' : 'García',
            'segundo_apellido' : 'Murillo',
            'calle' : 'Rafael Acuña',
            'numero' : 9,
            'colonia' : 'Artesanos',
            'codigo_postal' : 99343,
            'estado': test_view.agrega_estado(),
            'municipio': test_view.agrega_municipio(),
            'localidad': test_view.agrega_localidad(),
            'email' : 'garciamjuancarlos14@gmail.com',
            'telefono' : '4949428829',   
            'username' : 'juca',
            'password' : 'juca123'
        }
        self.archivos = {
            'ine' : SimpleUploadedFile('media/testfiles/ine.png', b'123456')
        }

    def test_login_usuario_vacio(self):
        self.crear_usuario()
        datos = {
            'username' : '',
            'password' : 'juca123'
        }
        form = AuthenticationForm(None, datos)
        self.assertFalse(form.is_valid())
        
    def test_login_contrasena_vacia(self):
        self.crear_usuario()
        datos = {
            'username' : 'juca',
            'password' : ''
        }
        form = AuthenticationForm(None, datos)
        self.assertFalse(form.is_valid())
        
    def test_login_con_usuario_y_contrasena_invalidos(self):
        self.crear_usuario()
        datos = {
            'username': 'usuarioinexistente',
            'password': 'noexisto123'
        }
        form = AuthenticationForm(None, datos)
        self.assertFalse(form.is_valid())
        
    def test_login_con_usuario_y_contrasena_validos(self):
        self.crear_usuario()
        datos = {
            'username': 'juca',
            'password': 'juca123'
        }
        form = AuthenticationForm(None, datos)
        self.assertTrue(form.is_valid())
        
    def test_usuario_form_valido(self):
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertTrue(form.is_valid())
        
    def test_nombre_longitud_excedida(self):
        self.usuario['first_name'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_primer_apellido_longitud_excedida(self):
        self.usuario['last_name'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_segundo_apellido_longitud_excedida(self):
        self.usuario['segundo_apellido'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_calle_longitud_excedida(self):
        self.usuario['calle'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_numero_menor_de_uno(self):
        self.usuario['numero'] = 0
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_numero_con_letras(self):
        self.usuario['numero'] = '123aa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_numero_excedido(self):
        self.usuario['numero'] = 10000
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_colonia_longitud_excedida(self):
        self.usuario['colonia'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_longitud_cuatro(self):
        self.usuario['codigo_postal'] = '9934'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_longitud_seis(self):
        self.usuario['codigo_postal'] = '993430'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_codigo_postal_con_letras(self):
        self.usuario['codigo_postal'] = '9934e'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_correo_longitud_excedida(self):
        self.usuario['email'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_correo_sin_arroba(self):
        self.usuario['email'] = 'jucagmail.com'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_correo_sin_dominio(self):
        self.usuario['email'] = 'juca@'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_telefono_longitud_once(self):
        self.usuario['telefono'] = '12345678901'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_telefono_longitud_nueve(self):
        self.usuario['telefono'] = '123456789'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_telefono_con_letras(self):
        self.usuario['telefono'] = '123a56789'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_ine_longitud_excedida(self):
        self.archivos['ine'] = 'media/testfiles/ineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.png'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
        
    def test_ine_extension_docx(self):
        self.archivos['ine'] = 'media/testfiles/ine.docx'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
            
    def test_usuario_longitud_excedida(self):
        self.usuario['username'] = 'jucaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
         
    def test_contra_longitud_excedida(self):
        self.usuario['password'] = 'jucaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        form = FormUsuario(self.usuario,files=self.archivos)
        self.assertFalse(form.is_valid())
           
    def crear_usuario(self):
        estado = Estado.objects.create(nombre='Zacatecas')
        municipio = Municipio.objects.create(nombre='Jerez', estado=estado)
        localidad = Localidad.objects.create(nombre='Jerez', municipio=municipio)
        
        Usuario.objects.create_user(
            first_name = 'Juan Carlos',
            last_name = 'García',
            calle = 'Rafael Acuña',
            numero = 9,
            colonia = 'Artesanos',
            codigo_postal = 99343,
            estado = estado,
            municipio = municipio,
            localidad = localidad,
            email = 'garciamjuancarlos14@gmail.com',
            telefono = '4949428829',
            ine = 'ine.png',
            username = 'juca',
            password = 'juca123'
        )
