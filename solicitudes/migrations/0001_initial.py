# Generated by Django 3.1.6 on 2021-12-05 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstatusSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(
                    '^[a-zA-Z\\s\\u00C0-\\u00FF]*$', 'Sólo se permiten letras.')], verbose_name='Nombre')),
                ('primer_apellido', models.CharField(max_length=35, validators=[django.core.validators.RegexValidator(
                    '^[a-zA-Z\\s\\u00C0-\\u00FF]*$', 'Sólo se permiten letras.')], verbose_name='Primer Apellido')),
                ('segundo_apellido', models.CharField(blank=True, max_length=35, null=True, validators=[django.core.validators.RegexValidator(
                    '^[a-zA-Z\\s\\u00C0-\\u00FF]*$', 'Sólo se permiten letras.')], verbose_name='Segundo apellido')),
                ('calle', models.CharField(max_length=34, verbose_name='Calle')),
                ('numero', models.PositiveIntegerField(validators=[
                 django.core.validators.MinValueValidator(1)], verbose_name='Número')),
                ('codigo_postal', models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(
                    5), django.core.validators.RegexValidator('^[0-9]*$', 'Sólo se permiten números.')], verbose_name='Código Postal')),
                ('seccion', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(
                    4), django.core.validators.RegexValidator('^[0-9]*$', 'Sólo se permiten números.')], verbose_name='Sección')),
                ('telefono', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(
                    10), django.core.validators.RegexValidator('^[0-9]*$', 'Sólo se permiten números.')], verbose_name='Teléfono')),
                ('curp', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(
                    '^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$')], verbose_name='CURP')),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(blank=True,
                 max_length=50, null=True, verbose_name='Correo')),
                ('resumen', models.TextField(blank=True, null=True,
                 verbose_name='Resumen de la solicitud')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
    ]
