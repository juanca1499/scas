from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


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
            'password': 'juca123',
        }
        form = AuthenticationForm(None, datos)
        self.assertTrue(form.is_valid())
        
    def crear_usuario(self):
        return User.objects.create_user(username='juca',password='juca123')
