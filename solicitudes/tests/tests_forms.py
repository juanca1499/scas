from django.test import TestCase

from solicitudes.forms import SolicitudForm
from solicitudes.models import EstadoCivil, Ocupacion, GradoEstudios


class TestForms(TestCase):
    def test_nombre_longitud_minima(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'J',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertTrue(form.is_valid())

    def test_nombre_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos Alfredo Román José de Jesús Marcos Germán',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_nombre_con_numeros(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos Alfredo Román José de Jesús 123',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_primer_apellido_longitud_minima(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'G',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertTrue(form.is_valid())

    def test_primer_apellido_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'asdasdasadasdsaassadasdasssddsaddsfd',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_primer_apellido_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'asdasdasadasdsaassadasdasssddsaddsfd',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_primer_apellido_sin_numeros(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García123',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_segundo_apellido_sin_numeros(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo123',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_segundo_apellido_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murilloooooooooooooooooooooooooooooo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_calle_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuñaaaaaaaaaaaaaaaaaaaaaaaa',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_calle_sin_numeros(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña 9',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_calle_sin_caracteres_especiales(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña .,.',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_numero_con_letras(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': '9nueve',
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_numero_en_cero(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 0,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': 4949428829,
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_codigo_postal_longitud_cuatro(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '9934',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_codigo_postal_longitud_seis(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '993411',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_codigo_postal_con_letras(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99tr',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_seccion_longitud_tres(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '062',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_seccion_longitud_cinco(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '06291',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_seccion_con_letras(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '062aa',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_telefono_nueve_digitos(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '494942882',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_telefono_once_digitos(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '49494288291',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_telefono_once_digitos(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '494942882a',
                'curp': 'GAMJ991014HZSRRN01',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_curp_sin_formato_valido(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_lugar_nacimiento_con_numeros(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas2',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_lugar_nacimiento_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecassssssssssssssssssssssssss',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_fecha_nacimiento_formato_dd_mm_aaaa(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '14-10-1999',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_fecha_nacimiento_formato_dd_mm_aa(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '14-10-99',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_fecha_nacimiento_formato_aa_mm_dd(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '99-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_otra_ocupacion_longitud_sobrepasada(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',
                'correo': 'garciamjuancarlos14@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_correo_sin_arroba(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlos14gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

    def test_correo_sin_arroba(self):
        self.agregar_estados_civiles()
        self.agregar_grados_estudios()
        self.agregar_ocupaciones()

        form = SolicitudForm(
            data={
                'fecha': '2021-11-17',
                'nombre': 'Juan Carlos',
                'primer_apellido': 'García',
                'segundo_apellido': 'Murillo',
                'calle': 'Rafael Acuña',
                'numero': 9,
                'codigo_postal': '99343',
                'seccion': '0629',
                'telefono': '4949428829',
                'curp': 'GAMJ991014HZSRRN',
                'lugar_nacimiento': 'Jerez, Zacatecas',
                'fecha_nacimiento': '1999-10-14',
                'estado_civil': EstadoCivil.objects.get(id=1),
                'ultimo_grado_estudios': GradoEstudios.objects.get(id=5),
                'ocupacion': Ocupacion.objects.get(id=1),
                'otra_ocupacion': 'Auxiliar',
                'correo': 'garciamjuancarlosssssssssssssssssssssssss@gmail.com',
                'resumen': 'El joven Juan Carlos es un estudiante universitario'
            }
        )
        self.assertFalse(form.is_valid())

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
