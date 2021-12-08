from django.test import TestCase
from django.db.utils import IntegrityError

from usuarios.models import Usuario, Estado, Municipio, Localidad


class TestModels(TestCase):

    def test_nombre_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name=None,
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_primer_apellido_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name=None,
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_calle_requerida(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle=None,
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_numero_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=None,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_colonia_requerida(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia=None,
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_codigo_postal_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=None,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_estado_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=None,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_municipio_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=None,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_localidad_requerida(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=None,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_telefono_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono=None,
                ine='ine.png',
                username='juca',
                password='juca123'
            )

    def test_dado_baja_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                dado_baja=None,
                username='juca',
                password='juca123'
            )

    def test_usuario_requerido(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        with self.assertRaises(ValueError):
            Usuario.objects.create_user(
                first_name='Juan Carlos',
                last_name='García',
                segundo_apellido='Murillo',
                calle='Rafael Acuña',
                numero=9,
                colonia='Artesanos',
                codigo_postal=99343,
                estado=estado,
                municipio=municipio,
                localidad=localidad,
                email='garciamjuancarlos14@gmail.com',
                telefono='4949428829',
                ine='ine.png',
                username=None,
                password='juca123'
            )

    def test_crear_usuario(self):
        estado = self.crear_estado()
        municipio = self.crear_municipio()
        localidad = self.crear_localidad()

        Usuario.objects.create_user(
            first_name='Juan Carlos',
            last_name='García',
            segundo_apellido='Murillo',
            calle='Rafael Acuña',
            numero=9,
            colonia='Artesanos',
            codigo_postal=99343,
            estado=estado,
            municipio=municipio,
            localidad=localidad,
            email='garciamjuancarlos14@gmail.com',
            telefono='4949428829',
            ine='ine.png',
            username='juca',
            password='juca123'
        )
        self.assertEqual(Usuario.objects.count(), 1)

    def crear_estado(self):
        return Estado.objects.create(nombre='Zacatecas')

    def crear_municipio(self):
        estado = Estado.objects.get(nombre='Zacatecas')
        return Municipio.objects.create(nombre='Jerez', estado=estado)

    def crear_localidad(self):
        municipio = Municipio.objects.get(nombre='Jerez')
        return Localidad.objects.create(nombre='Jerez', municipio=municipio)
