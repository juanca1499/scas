from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from usuarios.models import Estado, Municipio, Localidad, Usuario
from solicitudes.models import Solicitud, EstatusSolicitud
from solicitudes.views import ListaSolicitud, EditarSolicitud, NuevaSolicitud, DetalleSolicitud, obtiene_municipios, obtiene_localidades


class TestViews(TestCase):
    def setUp(self):
        self.solicitud = {
            'fecha': '2021-11-17',
            'nombre': 'Gabriel',
            'primer_apellido': 'Díaz',
            'segundo_apellido': 'Curiel',
            'calle': 'Montes de Oca',
            'numero': '3',
            'codigo_postal': '98613',
            'seccion': '0629',
            'telefono': '4941025153',
            'curp': 'DICC990912HZSZRS07',
            'fecha_nacimiento': '1999-09-12',
            'estado': None,
            'municipio': None,
            'localidad': None,
            'estatus': None,
            'correo': 'pruebas@gmail.com',
            'resumen': 'Solicitud 1'
        }
    
    def test_nueva_solicitud_form_valid(self):
        estatus = self.agrega_estatus()
        usuario = self.user_login()
        self.solicitud['estado'] = usuario.estado.id
        self.solicitud['municipio'] = usuario.municipio.id
        self.solicitud['localidad'] = usuario.localidad.id
        self.solicitud['estatus'] = estatus.id
        response = self.client.post('/solicitudes/nueva', self.solicitud)
        self.assertRedirects(response, '/solicitudes/')
        
    def test_nueva_solicitud_form_invalid(self):
        estatus = self.agrega_estatus()
        usuario = self.user_login()
        self.solicitud['estado'] = usuario.estado.id
        self.solicitud['municipio'] = usuario.municipio.id
        self.solicitud['localidad'] = usuario.localidad.id
        self.solicitud['estatus'] = estatus.id
        self.solicitud['fecha'] = 'a'
        response = self.client.post('/solicitudes/nueva', self.solicitud)
        form_solicitud = response.context['form']
        invalid = form_solicitud.is_valid()
        self.assertEqual(False, invalid)
            
    def test_editar_solicitud_form_valid(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        self.solicitud['estado'] = solicitud.estado.id
        self.solicitud['municipio'] = solicitud.municipio.id
        self.solicitud['localidad'] = solicitud.localidad.id
        self.solicitud['estatus'] = solicitud.estatus.id
        self.solicitud['nombre'] = 'César'
        self.solicitud['usuario'] = usuario.id
        response = self.client.post('/solicitudes/editar/'+str(solicitud.id), self.solicitud)
        self.assertRedirects(response, '/solicitudes/')
        
    def test_editar_solicitud_form_invalid(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        self.solicitud['estado'] = solicitud.estado.id
        self.solicitud['municipio'] = solicitud.municipio.id
        self.solicitud['localidad'] = solicitud.localidad.id
        self.solicitud['estatus'] = solicitud.estatus.id
        self.solicitud['codigo_postal'] = '981AF'
        self.solicitud['usuario'] = usuario.id
        response = self.client.post('/solicitudes/editar/'+str(solicitud.id), self.solicitud)
        form_solicitud = response.context['form']
        invalid = form_solicitud.is_valid()
        self.assertEqual(False, invalid)
        
    def test_context_lista_solicitudes(self):
        self.user_login()
        response = self.client.get('/solicitudes/')
        self.assertIsNotNone(response.context['solicitudes'])
        
    def test_redireccion_a_login_usuarios(self):
        response = self.client.get('/solicitudes/')
        self.assertRedirects(response, '/?next=/solicitudes/')
        
    def test_template_solicitudes_lista_admin(self):
        self.user_login()
        response = self.client.get('/solicitudes/')
        self.assertTemplateUsed(response, 'solicitudes/solicitud_list.html')
        
    def test_nombre_url_lista_solicitudes(self):
        self.user_login()
        response = self.client.get(reverse('solicitudes:lista'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_nueva_solicitud(self):
        self.user_login_admin()
        response = self.client.get('/solicitudes/nueva')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_nueva_solicitud(self):
        self.user_login()
        response = self.client.get(reverse('solicitudes:nueva'))
        self.assertEqual(response.status_code, 200)

    def test_template_nueva_solicitud(self):
        self.user_login()
        response = self.client.get('/solicitudes/nueva')
        self.assertTemplateUsed(response, 'solicitudes/solicitud_form.html')
    
    def test_lista_solicitudes_se_renderizo(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)
        response = self.client.get(reverse('solicitudes:lista'))
        self.assertTrue(response.is_rendered)    
    
    def test_url_solicitudes_editar(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/editar/'+str(solicitud.id))
        self.assertEqual(response.status_code, 200)
            
    def test_url_solicitudes_detalles(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertEqual(response.status_code, 200)

    def test_error_url_solicitudes_detalles_id_negativo(self):
        self.user_login()
        response = self.client.get('/solicitudes/detalle/'+str(-1))
        self.assertEqual(response.status_code, 404)

    def test_template_solicitudes_detalles(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertTemplateUsed(response, 'solicitudes/solicitud_detail.html') 
        
    def test_nombre_url_solicitudes_editar(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get(reverse('solicitudes:detalle', kwargs={'pk':solicitud.id,}) )
        self.assertEqual(response.status_code, 200)
        
    def test_envio_datos_solicitud_lista(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/')
        self.assertIn('solicitudes', response.context)
        
    def test_envio_datos_solicitud_detalles(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertIn('solicitud', response.context)
    
    def test_envio_CURP_datos_solicitud_lista(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)

        response = self.client.get('/solicitudes/')
        self.assertEquals('DICC990912HZSZRS07',
                          response.context['solicitudes'][0].curp)
        
    def test_envio_CURP_datos_solicitud_detalle(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        
        self.assertEquals('DICC990912HZSZRS07',
                          response.context['solicitud'].curp)

    def test_CURP_se_encuentre_en_template_lista(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/')
        self.assertContains(response, 'DICC990912HZSZRS07')
        
    def test_CURP_se_encuentre_en_template_detalles(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertContains(response, 'DICC990912HZSZRS07')
        
    def test_envio_modificacion_curp_datos_solicitud_lista(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)
        solicitud = Solicitud.objects.get(curp='DICC990912HZSZRS07')
        solicitud.curp = 'MADC990909HZSZRS08'
        solicitud.save()

        response = self.client.get('/solicitudes/')
        self.assertEquals('MADC990909HZSZRS08',
                          response.context['solicitudes'][0].curp)
        
    def test_envio_modificacion_curp_datos_solicitud_detalle(self):
        usuario = self.user_login()
        self.agrega_solicitud(usuario)
        solicitud = Solicitud.objects.get(curp='DICC990912HZSZRS07')
        solicitud.curp = 'MADC990909HZSZRS08'
        solicitud.save()

        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertEquals('MADC990909HZSZRS08',
                          response.context['solicitud'].curp)
        
    def test_agregar_solicitud_sin_loguearse(self):
        response = self.client.post('/solicitudes/nueva')
        self.assertEqual(response.status_code, 302)
        
    def test_editar_solicitud_sin_loguearse(self):
        response = self.client.post('/solicitudes/editar/1')
        self.assertEqual(response.status_code, 302)
        
    def test_ver_detalles_solicitud_sin_loguearse(self):
        response = self.client.post('/solicitudes/detalle/1')
        self.assertEqual(response.status_code, 302)
        
    def test_url_solicitudes_cargar_municipios_error(self):
        response = self.client.get('/solicitudes/municipios/')
        self.assertEqual(response.status_code, 403)
    
    def test_url_solicitudes_cargar_localidades_error(self):
        response = self.client.get('/solicitudes/localidades/')
        self.assertEqual(response.status_code, 403)
                                   
    def agrega_estatus(self):
        return EstatusSolicitud.objects.create(estatus='En Trámite')
    
    def agrega_estado(self):
        return Estado.objects.create(nombre='Zacatecas')
    
    def agrega_municipio(self):
        return Municipio.objects.create(
            nombre='Jerez',
            estado=self.agrega_estado(),
            )
        
    def agrega_localidad(self):
        return Localidad.objects.create(
            nombre='Cienega',
            municipio=self.agrega_municipio(),
            )

    def agrega_solicitud(self,usuario):
        return Solicitud.objects.create(
            fecha='2021-11-17',
            nombre='Gabriel',
            primer_apellido='Díaz',
            segundo_apellido='Curiel',
            calle='Montes de Oca',
            numero=3,
            codigo_postal=98613,
            seccion=int('0623'),
            telefono=4941025153,
            curp='DICC990912HZSZRS07',
            fecha_nacimiento='1999-09-12',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            estatus=self.agrega_estatus(),
            correo='pruebas@gmail.com',
            resumen='Solicitud 1',
            usuario=usuario
        )
    
    def user_login(self):
        usuario = Usuario.objects.create_user(
            username='gabriel12', 
            password='admin123',
            calle='Montes de Oca',
            numero=3,
            colonia='San francisco',
            codigo_postal='98613',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            telefono='4941025153',
            ine="imagen.png",
            dado_baja=0
        )
        self.client.login(username='gabriel12', password='admin123')
        return usuario
    
    def crear_usuario(self):
        usuario = Usuario.objects.create_user(
            username='gabriel12', 
            password='admin123',
            calle='Montes de Oca',
            numero=3,
            colonia='San francisco',
            codigo_postal='98613',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            telefono='4941025153',
            ine="imagen.png",
            dado_baja=0
        )
        return usuario
    
    def user_login_admin(self):
        usuario = User.objects.create_user(
            username='admin', password='admin123', is_superuser=1)
        self.client.login(username='admin', password='admin123')
        return usuario
