from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from usuarios.models import Usuario, Estado, Municipio, Localidad


class TestForms(TestCase):
    
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
