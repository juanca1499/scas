from django.test import TestCase
from django.contrib.auth.models import Permission

from usuarios.models import Usuario, Estado, Municipio, Localidad


class TestViews(TestCase):
    
    def test_login_usuario_y_contra_validos(self):
        self.crear_usuario_administrador()
        logueado = self.client.login(username='jucaadmin', password='juca123')
        self.assertTrue(logueado)
    
    def test_login_usuario_y_contra_invalidos(self):
        self.crear_usuario_administrador()
        logueado = self.client.login(username='jucaadmin', password='123')
        self.assertFalse(logueado)
          
    def test_registrar_usuario_sin_loguearse(self):
        response = self.client.post('/usuarios/nuevo')
        self.assertEqual(response.status_code, 302)
        
    def test_registrar_usuario_sin_permiso(self):
        self.iniciar_sesion_usuario_normal()
        response = self.client.post('/usuarios/nuevo')
        self.assertEqual(response.status_code, 403)
    
    def test_dar_de_baja_usuario_sin_loguearse(self):
        response = self.client.post('/usuarios/baja/1')
        self.assertEqual(response.status_code, 302)
        
    def test_dar_de_baja_usuario_sin_permiso(self):
        self.iniciar_sesion_usuario_normal()
        response = self.client.post('/usuarios/baja/1')
        self.assertEqual(response.status_code, 403)
        
    def test_editar_usuario_sin_loguearse(self):
        self.crear_usuario_normal()
        response = self.client.post('/usuarios/editar/1')
        self.assertEqual(response.status_code, 302)
        
    def test_editar_usuario_sin_permiso(self):
        self.iniciar_sesion_usuario_normal()
        response = self.client.post('/usuarios/editar/1')
        self.assertEqual(response.status_code, 403)
        
    def test_consultar_usuario_sin_loguearse(self):
        self.crear_usuario_normal()
        response = self.client.get('/usuarios/detalle/1')
        self.assertEqual(response.status_code, 302)
        
    def test_consultar_usuario_sin_permiso(self):
        self.iniciar_sesion_usuario_normal()
        response = self.client.get('/usuarios/detalle/1')
        self.assertEqual(response.status_code, 403)
        
    def test_consultar_lista_usuarios_sin_loguearse(self):
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 302)
        
    def test_consultar_lista_usuarios_sin_permiso(self):
        self.iniciar_sesion_usuario_normal()
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 403)
        
    def test_logout_sin_sesion_iniciada(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        
    def crear_usuario_normal(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        usuario = Usuario.objects.create_user(
            first_name = 'Juan Carlos',
            last_name = 'García',
            segundo_apellido = 'Murillo',
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
            password = 'juca123',
            is_superuser = False
        )
        return usuario
    
    def crear_usuario_administrador(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        usuario = Usuario.objects.create_user(
            first_name = 'Juan Carlos',
            last_name = 'García',
            segundo_apellido = 'Murillo',
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
            username = 'jucaadmin',
            password = 'juca123',
            is_superuser = True
        )
        return usuario
        
    def crear_estado(self):
        return Estado.objects.create(nombre='Zacatecas')
    
    def crear_municipio(self):
        estado = Estado.objects.get(nombre='Zacatecas')
        return Municipio.objects.create(nombre='Jerez',estado=estado)
    
    def crear_localidad(self):
        municipio = Municipio.objects.get(nombre='Jerez')
        return Localidad.objects.create(nombre='Jerez', municipio=municipio)      
    
    def iniciar_sesion_usuario_normal(self):
        usuario = self.crear_usuario_normal()
        self.client.login(username='juca', password='juca123')
        return usuario
    
    def iniciar_sesion_administrador(self):
        usuario = self.crear_usuario_administrador()
        self.client.login(username='jucaadmin', password='juca123')
        return usuario
