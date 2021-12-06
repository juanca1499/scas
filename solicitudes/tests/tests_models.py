from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from solicitudes.models import Solicitud, EstatusSolicitud
from usuarios.models import Estado, Municipio, Localidad, Usuario
from solicitudes.tests.tests_views import TestViews


class TestModels(TestCase):
    def test_humo(self):
        self.assertEqual(2 + 2, 4)
        
    def test_agrega_estatus_solicitud(self):
        estatus = EstatusSolicitud.objects.create(
            estatus='En Tramite'
        )

        estatus_1 = EstatusSolicitud.objects.first()

        self.assertEqual(estatus_1, estatus)
        self.assertEqual(estatus_1.estatus, 'En Tramite')
        self.assertEqual(str(estatus_1), 'En Tramite')
        self.assertEqual(len(EstatusSolicitud.objects.all()), 1)
        
    def test_agrega_estado(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )

        estado_1 = Estado.objects.first()

        self.assertEqual(estado_1, estado)
        self.assertEqual(estado_1.nombre, 'Zacatecas')
        self.assertEqual(len(Estado.objects.all()), 1)
        
    def test_agrega_municipio(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            nombre='Jerez',
            estado=estado
        )

        municipio_1 = Municipio.objects.first()

        self.assertEqual(municipio_1, municipio)
        self.assertEqual(municipio_1.nombre, 'Jerez')
        self.assertEqual(len(Municipio.objects.all()), 1)
        
        
    def test_agrega_localidad(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            nombre='Jerez',
            estado=estado
        )
        localidad = Localidad.objects.create(
            nombre='Cienega',
            municipio=municipio
        )

        localidad_1 = Localidad.objects.first()

        self.assertEqual(localidad_1, localidad)
        self.assertEqual(localidad_1.nombre, 'Cienega')
        self.assertEqual(len(Localidad.objects.all()), 1)
            
        
    def test_agrega_solicitud(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        solicitud = Solicitud.objects.create(
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
            estado=estado,
            municipio=municipio,
            localidad=localidad,
            estatus=estatus,
            correo='pruebas@gmail.com',
            resumen='Solicitud 1',
            usuario=self.agregar_usuario()
        )

        solicitud_1 = Solicitud.objects.first()

        self.assertEqual(solicitud, solicitud_1)
        self.assertEqual(solicitud.nombre, 'Gabriel')
        self.assertEqual(str(solicitud), 'DICC990912HZSZRS07')
        self.assertEqual(len(Solicitud.objects.all()), 1)

    def test_editar_solicitud(self):
        test_view = TestViews()
        usuario = self.agregar_usuario()
        solicitud = test_view.agrega_solicitud(usuario)

        solicitud_editada = Solicitud.objects.first()

        solicitud_editada.nombre = 'César'
        solicitud_editada.resumen = 'Solicitud actualizada'

        solicitud_1 = Solicitud.objects.first()

        self.assertEqual(solicitud_editada, solicitud_1)
        self.assertEqual(solicitud_editada.nombre, 'César')
        self.assertEqual(solicitud_editada.resumen, 'Solicitud actualizada')
        self.assertEqual(str(solicitud_editada), 'DICC990912HZSZRS07')
        self.assertEqual(len(Solicitud.objects.all()), 1)

    def test_fecha_requerida(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        
        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha=None,
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_nombre_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        
        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre=None,
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_primer_apellido_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido=None,
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_calle_requerida(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle=None,
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_numero_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=None,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_codigo_postal_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=None,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_seccion_requerida(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=None,
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_telefono_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=None,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_curp_requerida(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp=None,
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_fecha_nacimiento_requerida(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento=None,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )

    def test_estatus_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                estatus=None,
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )
            
    def test_estado_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=None,
                municipio=municipio,
                localidad=localidad,
                estatus=estatus,
                correo="garciamjuancarlos14@gmail.com",
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )
            
    def test_municipio_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=None,
                localidad=localidad,
                estatus=estatus,
                correo="garciamjuancarlos14@gmail.com",
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )
    
    def test_localidad_requerido(self):
        test_views = TestViews()
        estatus = test_views.agrega_estatus()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()

        with self.assertRaises(IntegrityError):
            Solicitud.objects.create(
                fecha='2021-11-17',
                nombre='Juan Carlos',
                primer_apellido='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                codigo_postal=99343,
                seccion=int('0629'),
                telefono=4949428829,
                curp='GAMJ991014HZSRRN01',
                fecha_nacimiento='1999-10-14',
                estado=estado,
                municipio=municipio,
                localidad=None,
                estatus=estatus,
                correo="garciamjuancarlos14@gmail.com",
                resumen='El joven Juan Carlos es un estudiante universitario',
                usuario=self.agregar_usuario()
            )
            
    def test_excede_longitud_nombre(self):
        test_view = TestViews()
        usuario = self.agregar_usuario()
        solicitud = test_view.agrega_solicitud(usuario)

        solicitud.nombre = 'Cesarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr'
        with self.assertRaises(ValidationError):
            solicitud.full_clean()
            
    def test_segundo_apellido_null(self):
        test_view = TestViews()
        usuario = self.agregar_usuario()
        solicitud = test_view.agrega_solicitud(usuario)
        solicitud.segundo_apellido = None

        self.assertEqual(solicitud.segundo_apellido, None)
        self.assertEqual(str(solicitud), 'DICC990912HZSZRS07')
        
    def test_actualiza_estatus(self):
        test_view = TestViews()
        estatus = test_view.agrega_estatus()
        usuario = self.agregar_usuario()
        solicitud = test_view.agrega_solicitud(usuario)

        solicitud.estatus = estatus
        estatus.estatus = 'Aceptado'

        self.assertEqual(solicitud.estatus, estatus)
        self.assertEqual(str(solicitud.estatus), 'Aceptado')
    
    def agregar_usuario(self):
        test_view = TestViews()
        usuario = Usuario.objects.create_user(
            username='gabriel12', 
            password='admin123',
            calle='Montes de Oca',
            numero=3,
            colonia='San francisco',
            codigo_postal='98613',
            estado=test_view.agrega_estado(),
            municipio=test_view.agrega_municipio(),
            localidad=test_view.agrega_localidad(),
            telefono='4941025153',
            ine="imagen.png",
            dado_baja=False
        )
        return usuario