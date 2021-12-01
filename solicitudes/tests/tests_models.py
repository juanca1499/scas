from django.test import TestCase
from django.db.utils import IntegrityError

from solicitudes.models import Solicitud, EstadoCivil,\
    Ocupacion, GradoEstudios


class TestModels(TestCase):
    def test_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_nombre_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_nombre_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_primer_apellido_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_calle_requerida(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_numero_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_codigo_postal_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_seccion_requerida(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_telefono_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_curp_requerida(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_lugar_nacimiento_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento=None,
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_fecha_nacimiento_requerida(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento=None,
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_estado_civil_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=None,
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_ultimo_grado_estudio_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=None,
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_ocupacion_requerida(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=None,
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_correo_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo=None,
                resumen='El joven Juan Carlos es un estudiante universitario'
            )

    def test_resumen_solicitud_requerido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

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
                lugar_nacimiento='Jerez, Zacatecas',
                fecha_nacimiento='1999-10-14',
                estado_civil=EstadoCivil.objects.get(id=1),
                ultimo_grado_estudios=GradoEstudios.objects.get(id=5),
                ocupacion=Ocupacion.objects.get(id=1),
                otra_ocupacion='Auxiliar',
                correo='garciamjuancarlos14@gmail.com',
                resumen=None
            )

    def agregar_estados_civiles(self):
        EstadoCivil.objects.create(estado_civil='Soltero(a)')
        EstadoCivil.objects.create(estado_civil='Unión libre')
        EstadoCivil.objects.create(estado_civil='Casado(a)')
        EstadoCivil.objects.create(estado_civil='Separado(a)')
        EstadoCivil.objects.create(estado_civil='Viudo(a)')
        EstadoCivil.objects.create(estado_civil='No sabe')
        EstadoCivil.objects.create(estado_civil='Divorciado(a)')

    def agregar_grados_estudios(self):
        GradoEstudios.objects.create(grado='Ninguna')
        GradoEstudios.objects.create(grado='Primaria')
        GradoEstudios.objects.create(grado='Secundaria')
        GradoEstudios.objects.create(grado='Bachillerato')
        GradoEstudios.objects.create(grado='Técnico')
        GradoEstudios.objects.create(grado='Universidad')
        GradoEstudios.objects.create(grado='Otros')

    def agregar_ocupaciones(self):
        Ocupacion.objects.create(ocupacion='Estudiante')
        Ocupacion.objects.create(ocupacion='Hogar')
        Ocupacion.objects.create(ocupacion='Empleado')
        Ocupacion.objects.create(ocupacion='Empleado de gobierno')
        Ocupacion.objects.create(ocupacion='Obrero')
        Ocupacion.objects.create(ocupacion='Profesionista')
        Ocupacion.objects.create(ocupacion='Agricultor')
        Ocupacion.objects.create(ocupacion='Ganadero')
        Ocupacion.objects.create(ocupacion='Jornalero')
        Ocupacion.objects.create(ocupacion='Eventual')
        Ocupacion.objects.create(ocupacion='Pensionado(a)')
        Ocupacion.objects.create(ocupacion='Jubilado(a)')
