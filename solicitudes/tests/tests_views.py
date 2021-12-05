from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from usuarios.models import Estado, Municipio, Localidad, Usuario
from solicitudes.models import Solicitud, EstatusSolicitud
from solicitudes.views import ListaSolicitud, EditarSolicitud, NuevaSolicitud, DetalleSolicitud


class TestViews(TestCase):
    
    def test_url_solicitudes_lista(self):
        self.user_login()
        response = self.client.get('/solicitudes/')
        self.assertEqual(response.status_code, 200)
        
    def test_template_solicitudes_lista(self):
        self.user_login()
        response = self.client.get('/solicitudes/')
        self.assertTemplateUsed(response, 'solicitudes/solicitud_list.html')
        
    def test_nombre_url_lista_solicitudes(self):
        self.user_login()
        response = self.client.get(reverse('solicitudes:lista'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_nueva_solicitud(self):
        self.user_login()
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
        
    def test_url_solicitudes_editar(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/editar/'+str(solicitud.id))
        self.assertEqual(response.status_code, 200)

    def test_error_url_solicitudes_editar_id_negativo(self):
        self.user_login()
        response = self.client.get('/solicitudes/editar/'+str(-1))
        self.assertEqual(response.status_code, 404)

    def test_template_solicitudes_editar(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/editar/'+str(solicitud.id))
        self.assertTemplateUsed(response, 'solicitudes/solicitud_form.html')   
        
    def test_url_solicitudes_detalles(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertEqual(response.status_code, 200)

    def test_error_url_solicitudes_detalles_id_negativo(self):
        self.user_login()
        response = self.client.get('/solicitudes/detalle/'+str(-1))
        self.assertEqual(response.status_code, 404)

    def test_template_solicitudes_detalles(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertTemplateUsed(response, 'solicitudes/solicitud_detail.html') 
        
    def test_envio_datos_solicitud_lista(self):
        self.user_login()
        self.agrega_solicitud()
        response = self.client.get('/solicitudes/')
        self.assertIn('solicitudes', response.context)
        
    def test_envio_datos_solicitud_detalles(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertIn('solicitud', response.context)
    
    def test_envio_CURP_datos_solicitud_lista(self):
        self.user_login()
        self.agrega_solicitud()

        response = self.client.get('/solicitudes/')
        self.assertEquals('DICC990912HZSZRS07',
                          response.context['solicitudes'][0].curp)
        
    def test_envio_CURP_datos_solicitud_detalle(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        
        self.assertEquals('DICC990912HZSZRS07',
                          response.context['solicitud'].curp)

    def test_CURP_se_encuentre_en_template_lista(self):
        self.user_login()
        self.agrega_solicitud()
        response = self.client.get('/solicitudes/')
        self.assertContains(response, 'DICC990912HZSZRS07')
        
    def test_CURP_se_encuentre_en_template_detalles(self):
        self.user_login()
        solicitud = self.agrega_solicitud()
        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertContains(response, 'DICC990912HZSZRS07')
        
    def test_envio_modificacion_curp_datos_solicitud_lista(self):
        self.user_login()
        self.agrega_solicitud()
        solicitud = Solicitud.objects.get(curp='DICC990912HZSZRS07')
        solicitud.curp = 'MADC990909HZSZRS08'
        solicitud.save()

        response = self.client.get('/solicitudes/')
        self.assertEquals('MADC990909HZSZRS08',
                          response.context['solicitudes'][0].curp)
        
    def test_envio_modificacion_curp_datos_solicitud_detalle(self):
        self.user_login()
        self.agrega_solicitud()
        solicitud = Solicitud.objects.get(curp='DICC990912HZSZRS07')
        solicitud.curp = 'MADC990909HZSZRS08'
        solicitud.save()

        response = self.client.get('/solicitudes/detalle/'+str(solicitud.id))
        self.assertEquals('MADC990909HZSZRS08',
                          response.context['solicitud'].curp)

    def agrega_estatus(self):
        return EstatusSolicitud.objects.create(estatus='En Tramite')
    
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

    def agrega_solicitud(self):
        usuario = self.crear_usuario()
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
        usuario = User.objects.create_user(
            username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')
        return usuario
    
    def crear_usuario(self):
        usuario = Usuario.objects.create_user(
            username='gabriel12', 
            password='admin123',
            calle='Montes de Oca',
            numero=3,
            colonia='San francisco',
            codigo_postal=98613,
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            telefono=4941025153,
            ine="imagen.png",
            dado_baja=False
        )
        return usuario
