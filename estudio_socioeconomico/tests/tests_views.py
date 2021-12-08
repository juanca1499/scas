from django.http import response
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Permission
from solicitudes.models import EstatusSolicitud, Solicitud
from usuarios.models import Estado, Municipio, Localidad, Usuario

from estudio_socioeconomico.models import * 

class TestViews(TestCase):
    def setUp(self):
        self.estudio = {
            'fecha_actual' : '2021-11-17',
            'credencial' : None,
            'comprobante_domicilio' : None,
            'escolaridad' : None,
            'solicitud':None,
            'edad' : '20',
            'calle' : 'Adelitas revolucionarias',
            'numero_exterior' : '9',
            'colonia' : 'Adelitas',
            'codigo_postal' : '98613',
            'estado' : None,
            'municipio' : None,
            'localidad' : None,
            'telefono' : '4921736547',
            'cabeza_familia' : True,
            'estado_civil' : None,
            'discapacidad' : None,
            'tres_planta' : True,
            'sala_comedor' : True ,
            'cocina' : True,
            'numero_recamaras' : '1',
            'numero_banios' : '2',
            'piso_es' : None,
            'techo_es' : None,
            'automovil' : None,
            'tipo_combustible' : None,
            'casa_es' : None,
            'casa_energia' : True,
            'casa_drenaje' : True,
            'ocupacion' : None,
            'servicio_salud' : None,
            'enfermedad_cancer' : True,
            'enfermedad_quemaduras' : True,
            'enfermedad_epilepsia' : True
        }
    
    def test_url_estudios_lista(self):
        self.user_login()
        response = self.client.get('/estudio-socieconomico/')
        self.assertEqual(response.status_code, 200)
        
    def test_estudios_agregar_estudio_view_invalido(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        datos = {}
        response = self.client.get('/estudio-socieconomico/nuevo/'+str(solicitud.id),datos)
        self.assertEqual(response.status_code, 200)
        
    def test_estudios_editar_estudio_view_invalido(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        datos = {}
        response = self.client.get('/estudio-socieconomico/editar/'+str(estudio.folio),datos)
        self.assertEqual(response.status_code, 200)
        
    def test_template_estudios_lista(self):
        self.user_login()
        response = self.client.get('/estudio-socieconomico/')
        self.assertTemplateUsed(response, 'estudio_socioeconomico/estudio_list.html')
        
    def test_nombre_url_lista_estudios(self):
        self.user_login()
        response = self.client.get(reverse('estudio_socioeconomico:lista'))
        self.assertEqual(response.status_code, 200)
            
    def test_url_nuevo_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get(reverse('estudio_socioeconomico:nuevo',args=[solicitud.id]))
        self.assertEqual(response.status_code, 200)
        
    def test_template_nuevo_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        response = self.client.get(reverse('estudio_socioeconomico:nuevo',args=[solicitud.id]))
        self.assertTemplateUsed(response, 'estudio_socioeconomico/estudio_form.html')        
        
    def test_template_editar_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:editar',args=[estudio.folio]))
        self.assertTemplateUsed(response, 'estudio_socioeconomico/estudio_form.html')   
        
    def test_url_editar_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:editar',args=[estudio.folio]))
        self.assertEqual(response.status_code, 200)     

    def test_error_url_editar_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:editar',args=[-34]))
        self.assertEqual(response.status_code, 404) 
        
    def test_template_detalle_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:detalle',args=[estudio.folio]))
        self.assertTemplateUsed(response, 'estudio_socioeconomico/estudio_detail.html')   
        
    def test_url_detalle_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:detalle',args=[estudio.folio]))
        self.assertEqual(response.status_code, 200)     

    def test_error_url_detalle_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:detalle',args=[-34]))
        self.assertEqual(response.status_code, 404) 
        
        
    def test_folio_en_lista_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:lista'))
        self.assertContains(response, estudio.folio)
        
    def test_nombre_en_lista_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:lista'))
        self.assertContains(response,estudio.solicitud.nombre)
        
    def test_primer_apellido_en_lista_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:lista'))
        self.assertContains(response,estudio.solicitud.primer_apellido)
        
    def test_segundo_apellido_en_lista_estudio(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio = self.agrega_estudio(solicitud)
        response = self.client.get(reverse('estudio_socioeconomico:lista'))
        self.assertContains(response,estudio.solicitud.segundo_apellido)
        
    def test_url_estudios_editar_view(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio1 = self.agrega_estudio(solicitud)
        self.estudio['solicitud'] = solicitud
        self.estudio['credencial'] = estudio1.credencial
        self.estudio['comprobante_domicilio'] = estudio1.comprobante_domicilio
        self.estudio['escolaridad'] = self.agrega_escolaridad().id
        self.estudio['estado'] = self.agrega_estado().id
        self.estudio['municipio'] = self.agrega_municipio().id
        self.estudio['localidad'] = self.agrega_localidad().id
        self.estudio['estado_civil'] = self.agrega_estado_civil().id
        self.estudio['discapacidad'] = self.agrega_discapacidad().id
        self.estudio['piso_es'] = self.agrega_piso().id
        self.estudio['techo_es'] = self.agrega_techo().id
        self.estudio['automovil'] = self.agrega_automovil().id
        self.estudio['tipo_combustible'] = self.agrega_tipo_combustible().id
        self.estudio['casa_es'] = self.agrega_casa().id
        self.estudio['ocupacion'] = estudio1.ocupacion.id
        self.estudio['servicio_salud'] = estudio1.servicio_salud.id
        response = self.client.post('/estudio-socieconomico/editar/'+str(estudio1.folio),self.estudio)
        self.assertEqual(response.status_code, 302)
        
    def test_url_estudios_nuevo_view(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio1 = self.agrega_estudio(solicitud)
        solicitud2 = self.agrega_solicitud(usuario)
        self.estudio['solicitud'] = solicitud2
        self.estudio['credencial'] = estudio1.credencial
        self.estudio['comprobante_domicilio'] = estudio1.comprobante_domicilio
        self.estudio['escolaridad'] = self.agrega_escolaridad().id
        self.estudio['estado'] = self.agrega_estado().id
        self.estudio['municipio'] = self.agrega_municipio().id
        self.estudio['localidad'] = self.agrega_localidad().id
        self.estudio['estado_civil'] = self.agrega_estado_civil().id
        self.estudio['discapacidad'] = self.agrega_discapacidad().id
        self.estudio['piso_es'] = self.agrega_piso().id
        self.estudio['techo_es'] = self.agrega_techo().id
        self.estudio['automovil'] = self.agrega_automovil().id
        self.estudio['tipo_combustible'] = self.agrega_tipo_combustible().id
        self.estudio['casa_es'] = self.agrega_casa().id
        self.estudio['ocupacion'] = estudio1.ocupacion.id
        self.estudio['servicio_salud'] = estudio1.servicio_salud.id
        
        response = self.client.post('/estudio-socieconomico/nuevo/'+str(solicitud2.id),self.estudio)
        self.assertEqual(response.status_code, 302)
        
    def test_url_estudios_editar_view_form_invalid(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio1 = self.agrega_estudio(solicitud)
        self.estudio['solicitud'] = solicitud
        self.estudio['credencial'] = estudio1.credencial
        self.estudio['comprobante_domicilio'] = estudio1.comprobante_domicilio
        self.estudio['escolaridad'] = self.agrega_escolaridad().id
        self.estudio['estado'] = self.agrega_estado().id
        self.estudio['municipio'] = self.agrega_municipio().id
        self.estudio['localidad'] = self.agrega_localidad().id
        self.estudio['estado_civil'] = self.agrega_estado_civil().id
        self.estudio['discapacidad'] = self.agrega_discapacidad().id
        self.estudio['piso_es'] = self.agrega_piso().id
        self.estudio['techo_es'] = self.agrega_techo().id
        self.estudio['automovil'] = self.agrega_automovil().id
        self.estudio['tipo_combustible'] = self.agrega_tipo_combustible().id
        self.estudio['casa_es'] = self.agrega_casa().id
        self.estudio['ocupacion'] = estudio1.ocupacion.id
        self.estudio['servicio_salud'] = estudio1.servicio_salud.id
        self.estudio['fecha_actual'] = 'a'
        response = self.client.post('/estudio-socieconomico/editar/'+str(estudio1.folio),self.estudio)
        self.assertEqual(response.status_code, 200)
        
    def test_url_estudios_nuevo_view_form_invalid(self):
        usuario = self.user_login()
        solicitud = self.agrega_solicitud(usuario)
        estudio1 = self.agrega_estudio(solicitud)
        solicitud2 = self.agrega_solicitud(usuario)
        self.estudio['solicitud'] = solicitud2
        self.estudio['credencial'] = estudio1.credencial
        self.estudio['comprobante_domicilio'] = estudio1.comprobante_domicilio
        self.estudio['escolaridad'] = self.agrega_escolaridad().id
        self.estudio['estado'] = self.agrega_estado().id
        self.estudio['municipio'] = self.agrega_municipio().id
        self.estudio['localidad'] = self.agrega_localidad().id
        self.estudio['estado_civil'] = self.agrega_estado_civil().id
        self.estudio['discapacidad'] = self.agrega_discapacidad().id
        self.estudio['piso_es'] = self.agrega_piso().id
        self.estudio['techo_es'] = self.agrega_techo().id
        self.estudio['automovil'] = self.agrega_automovil().id
        self.estudio['tipo_combustible'] = self.agrega_tipo_combustible().id
        self.estudio['casa_es'] = self.agrega_casa().id
        self.estudio['ocupacion'] = estudio1.ocupacion.id
        self.estudio['servicio_salud'] = estudio1.servicio_salud.id
        self.estudio['fecha_actual'] = 'a'
        response = self.client.post('/estudio-socieconomico/nuevo/'+str(solicitud2.id),self.estudio)
        self.assertEqual(response.status_code, 200)
            
    def agrega_escolaridad(self):
        return Escolaridad.objects.create(escolaridad ='Ninguna')

    def agrega_estado_civil(self):
        return EstadoCivil.objects.create(estado_civil ='Soltero (a)')
    
    def agrega_discapacidad(self):
        return Discapacidad.objects.create(discapacidad ='Ninguna')
    
    def agrega_piso(self):
        return Piso.objects.create(piso='Concreto')
    
    def agrega_techo(self):
        return Techo.objects.create(techo='Lamina')
    
    def agrega_automovil(self):
        return Automovil.objects.create(automovil='Prestado')
    
    def agrega_tipo_combustible(self):
        return TipoCombustible.objects.create(tipo_combustible='Gasolina')
    
    def agrega_ocupacion(self):
        return Ocupacion.objects.create(ocupacion='Profesionista')
    
    def agrega_casa(self):
        return CasaEs.objects.create(casa_es='Propia, pagada y escriturada')
    
    def agrega_servicio_salud(self):
        return ServicioSalud.objects.create(servicio='INSABI')
    
    def agrega_estado(self):
        return Estado.objects.create(nombre='Zacatecas')
    
    def agrega_municipio(self):
        return Municipio.objects.create(
            nombre='Guadalupe',
            estado=self.agrega_estado(),
            )
       
    def agrega_localidad(self):
        return Localidad.objects.create(
            nombre='Tacoaleche',
            municipio=self.agrega_municipio(),
            )
        
    def agrega_estatus(self):
        return EstatusSolicitud.objects.create(estatus='En Tramite')
        
    def agrega_estudio(self,solicitud):
        return EstudioSocioeconomico.objects.create(
            fecha_actual = '2021-11-17',
            credencial = 'testfiles/ine.png',
            comprobante_domicilio = 'testfiles/comprobante.png',
            escolaridad = self.agrega_escolaridad(),
            solicitud = solicitud,
            edad = 20,
            calle = 'Adelitas revolucionarias',
            numero_exterior = 9,
            colonia = 'Adelitas',
            codigo_postal = 98613,
            estado = self.agrega_estado(),
            municipio = self.agrega_municipio(),
            localidad = self.agrega_localidad(),
            telefono = '4921736547',
            cabeza_familia = True,
            estado_civil = self.agrega_estado_civil(),
            discapacidad = self.agrega_discapacidad(),
            tres_planta = True,
            sala_comedor = True ,
            cocina = True,
            numero_recamaras = 1,
            numero_banios = 2,
            piso_es = self.agrega_piso(),
            techo_es = self.agrega_techo(),
            automovil = self.agrega_automovil(),
            tipo_combustible = self.agrega_tipo_combustible(),
            casa_es = self.agrega_casa(),
            casa_energia = True,
            casa_drenaje = True,
            ocupacion = self.agrega_ocupacion(),
            servicio_salud = self.agrega_servicio_salud(),
            enfermedad_cancer = True,
            enfermedad_quemaduras = True,
            enfermedad_epilepsia = True
        )    

    def user_login(self):
        usuario = Usuario.objects.create_user(
            username='josue_3', 
            password='josue123',
            calle='Real de Angeles',
            numero=43,
            colonia='Camino Real',
            codigo_postal='98613',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            telefono='492736547',
            ine="imagen.png",
            dado_baja=0
        )
        self.client.login(username='josue_3', password='josue123')
        return usuario
    
    def agrega_solicitud(self,usuario):
        return Solicitud.objects.create(
            fecha='2021-11-17',
            nombre='Josue',
            primer_apellido='González',
            segundo_apellido='Pinedo',
            calle='real de Angeles',
            numero=43,
            codigo_postal=98613,
            seccion=int('0623'),
            telefono=4921736547,
            curp='GOPJ990929HZSNNS07',
            fecha_nacimiento='1999-09-29',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            estatus=self.agrega_estatus(),
            correo='pruebas@gmail.com',
            resumen='Solicitud 1',
            usuario=usuario
        )
        
    def agrega_usuario(self):
        usuario = Usuario.objects.create_user(
            username='josue_3', 
            password='josue123',
            calle='Real de Angeles',
            numero=43,
            colonia='Camino Real',
            codigo_postal='98613',
            estado=self.agrega_estado(),
            municipio=self.agrega_municipio(),
            localidad=self.agrega_localidad(),
            telefono='492736547',
            ine="imagen.png",
            dado_baja=0
        )
        return usuario