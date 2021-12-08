from django import test
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from estudio_socioeconomico.tests.tests_views import TestViews
from usuarios.models import Estado, Municipio, Localidad, Usuario
from solicitudes.models import Solicitud, EstatusSolicitud
from estudio_socioeconomico.models import *


class TestModels(TestCase):

    def test_agrega_escolaridad(self):
        escolaridad = Escolaridad.objects.create(escolaridad='Ninguna')

        escolaridad_1 = Escolaridad.objects.first()

        self.assertEqual(escolaridad_1, escolaridad)
        self.assertEqual(escolaridad_1.escolaridad, 'Ninguna')
        self.assertEqual(str(escolaridad_1), 'Ninguna')
        self.assertEqual(len(Escolaridad.objects.all()), 1)

    def test_agrega_estado_civil(self):
        estado_civil = EstadoCivil.objects.create(estado_civil='Soltero (a)')

        estado_civil_1 = EstadoCivil.objects.first()

        self.assertEqual(estado_civil_1, estado_civil)
        self.assertEqual(estado_civil_1.estado_civil, 'Soltero (a)')
        self.assertEqual(str(estado_civil_1), 'Soltero (a)')
        self.assertEqual(len(EstadoCivil.objects.all()), 1)

    def test_agrega_discapacidad(self):
        discapacidad = Discapacidad.objects.create(discapacidad='Ninguna')

        discapacidad_1 = Discapacidad.objects.first()

        self.assertEqual(discapacidad_1, discapacidad)
        self.assertEqual(discapacidad_1.discapacidad, 'Ninguna')
        self.assertEqual(str(discapacidad_1), 'Ninguna')
        self.assertEqual(len(Discapacidad.objects.all()), 1)

    def test_agrega_piso(self):
        piso = Piso.objects.create(piso='Concreto')

        piso_1 = Piso.objects.first()

        self.assertEqual(piso_1, piso)
        self.assertEqual(piso_1.piso, 'Concreto')
        self.assertEqual(str(piso_1), 'Concreto')
        self.assertEqual(len(Piso.objects.all()), 1)

    def test_agrega_techo(self):
        techo = Techo.objects.create(techo='Lamina')

        techo_1 = Techo.objects.first()

        self.assertEqual(techo_1, techo)
        self.assertEqual(techo_1.techo, 'Lamina')
        self.assertEqual(str(techo_1), 'Lamina')
        self.assertEqual(len(Techo.objects.all()), 1)

    def test_agrega_automovil(self):
        automovil = Automovil.objects.create(automovil='Prestado')

        automovil_1 = Automovil.objects.first()

        self.assertEqual(automovil_1, automovil)
        self.assertEqual(automovil_1.automovil, 'Prestado')
        self.assertEqual(str(automovil_1), 'Prestado')
        self.assertEqual(len(Automovil.objects.all()), 1)

    def test_agrega_tipo_combustible(self):
        tipo_combustible = TipoCombustible.objects.create(
            tipo_combustible='Gasolina')

        tipo_combustible_1 = TipoCombustible.objects.first()

        self.assertEqual(tipo_combustible_1, tipo_combustible)
        self.assertEqual(tipo_combustible_1.tipo_combustible, 'Gasolina')
        self.assertEqual(str(tipo_combustible_1), 'Gasolina')
        self.assertEqual(len(TipoCombustible.objects.all()), 1)

    def test_agrega_ocupacion(self):
        ocupacion = Ocupacion.objects.create(ocupacion='Profesionista')

        ocupacion_1 = Ocupacion.objects.first()

        self.assertEqual(ocupacion_1, ocupacion)
        self.assertEqual(ocupacion_1.ocupacion, 'Profesionista')
        self.assertEqual(str(ocupacion_1), 'Profesionista')
        self.assertEqual(len(Ocupacion.objects.all()), 1)

    def test_agrega_casa(self):
        casa_es = CasaEs.objects.create(casa_es='Propia, pagada y escriturada')

        casa_es_1 = CasaEs.objects.first()

        self.assertEqual(casa_es_1, casa_es)
        self.assertEqual(casa_es_1.casa_es, 'Propia, pagada y escriturada')
        self.assertEqual(str(casa_es_1), 'Propia, pagada y escriturada')
        self.assertEqual(len(CasaEs.objects.all()), 1)

    def test_agrega_servicio_salud(self):
        servicio = ServicioSalud.objects.create(servicio='INSABI')

        servicio_1 = ServicioSalud.objects.first()

        self.assertEqual(servicio_1, servicio)
        self.assertEqual(servicio_1.servicio, 'INSABI')
        self.assertEqual(str(servicio_1), 'INSABI')
        self.assertEqual(len(ServicioSalud.objects.all()), 1)

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
            nombre='Guadalupe',
            estado=estado
        )

        municipio_1 = Municipio.objects.first()

        self.assertEqual(municipio_1, municipio)
        self.assertEqual(municipio_1.nombre, 'Guadalupe')
        self.assertEqual(len(Municipio.objects.all()), 1)

    def test_agrega_localidad(self):
        estado = Estado.objects.create(
            nombre='Zacatecas'
        )
        municipio = Municipio.objects.create(
            nombre='Guadalupe',
            estado=estado
        )
        localidad = Localidad.objects.create(
            nombre='Tacoaleche',
            municipio=municipio
        )

        localidad_1 = Localidad.objects.first()

        self.assertEqual(localidad_1, localidad)
        self.assertEqual(localidad_1.nombre, 'Tacoaleche')
        self.assertEqual(len(Localidad.objects.all()), 1)

    def test_agrega_estudio(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        estudio = EstudioSocioeconomico.objects.create(
            fecha_actual='2021-11-17',
            credencial='ine.png',
            comprobante_domicilio='comprobante.png',
            escolaridad=escolaridad,
            solicitud=solicitud,
            edad=20,
            calle='Adelitas revolucionarias',
            numero_exterior=9,
            colonia='Adelitas',
            codigo_postal=98613,
            estado=estado,
            municipio=municipio,
            localidad=localidad,
            telefono='4921736547',
            cabeza_familia=True,
            estado_civil=estado_civil,
            discapacidad=discapacidad,
            tres_planta=True,
            sala_comedor=True,
            cocina=True,
            numero_recamaras=1,
            numero_banios=2,
            piso_es=piso,
            techo_es=techo,
            automovil=automovil,
            tipo_combustible=tipo_combustible,
            casa_es=casa_es,
            casa_energia=True,
            casa_drenaje=True,
            ocupacion=ocupacion,
            servicio_salud=servicio_salud,
            enfermedad_cancer=True,
            enfermedad_quemaduras=True,
            enfermedad_epilepsia=True
        )

        estudio_1 = EstudioSocioeconomico.objects.first()

        self.assertEqual(estudio, estudio_1)
        self.assertEqual(estudio.calle, 'Adelitas revolucionarias')
        self.assertEqual(estudio.telefono, '4921736547')
        self.assertEqual(len(EstudioSocioeconomico.objects.all()), 1)

    def test_editar_estudio(self):
        test_view = TestViews()
        usuario = test_view.agrega_usuario()
        solicitud = test_view.agrega_solicitud(usuario)
        estudio = test_view.agrega_estudio(solicitud)

        estudio_editado = EstudioSocioeconomico.objects.first()

        estudio_editado.colonia = 'Camino Real'
        estudio_editado.edad = 18

        estudio_1 = EstudioSocioeconomico.objects.first()

        self.assertEqual(estudio_editado, estudio_1)
        self.assertEqual(estudio_editado.colonia, 'Camino Real')
        self.assertEqual(estudio_editado.edad, 18)
        self.assertEqual(len(EstudioSocioeconomico.objects.all()), 1)

    def test_editar_estudio(self):
        test_view = TestViews()
        usuario = test_view.agrega_usuario()
        solicitud = test_view.agrega_solicitud(usuario)
        estudio = test_view.agrega_estudio(solicitud)

        estudio_editado = EstudioSocioeconomico.objects.first()

        estudio_editado.colonia = 'Camino Real'
        estudio_editado.edad = 18

        estudio_1 = EstudioSocioeconomico.objects.first()

        self.assertEqual(estudio_editado, estudio_1)
        self.assertEqual(estudio_editado.colonia, 'Camino Real')
        self.assertEqual(estudio_editado.edad, 18)
        self.assertEqual(len(EstudioSocioeconomico.objects.all()), 1)

    def test_escolaridad_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=None,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_estado_civil_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=None,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_discapacidad_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=None,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_piso_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=None,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_techo_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=None,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_automovil_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=None,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_tipo_combustible_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=None,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud,
            )

    def test_casa_es_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=None,
                ocupacion=ocupacion,
                servicio_salud=servicio_salud
            )

    def test_ocupacion_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=None,
                servicio_salud=servicio_salud
            )

    def test_servicio_salud_requerida(self):
        test_views = TestViews()
        estado = test_views.agrega_estado()
        municipio = test_views.agrega_municipio()
        localidad = test_views.agrega_localidad()
        solicitud = test_views.agrega_solicitud(test_views.agrega_usuario())
        escolaridad = test_views.agrega_escolaridad()
        estado_civil = test_views.agrega_estado_civil()
        discapacidad = test_views.agrega_discapacidad()
        piso = test_views.agrega_piso()
        techo = test_views.agrega_techo()
        automovil = test_views.agrega_automovil()
        tipo_combustible = test_views.agrega_tipo_combustible()
        ocupacion = test_views.agrega_ocupacion()
        casa_es = test_views.agrega_casa()
        servicio_salud = test_views.agrega_servicio_salud()

        with self.assertRaises(IntegrityError):
            EstudioSocioeconomico.objects.create(
                fecha_actual='2021-11-17',
                credencial='ine.png',
                comprobante_domicilio='comprobante.png',
                escolaridad=escolaridad,
                solicitud=solicitud,
                edad=20,
                calle='Adelitas revolucionarias',
                numero_exterior=9,
                colonia='Adelitas',
                codigo_postal=98613,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                telefono='4921736547',
                estado_civil=estado_civil,
                discapacidad=discapacidad,
                numero_recamaras=1,
                numero_banios=2,
                piso_es=piso,
                techo_es=techo,
                automovil=automovil,
                tipo_combustible=tipo_combustible,
                casa_es=casa_es,
                ocupacion=ocupacion,
                servicio_salud=None
            )
