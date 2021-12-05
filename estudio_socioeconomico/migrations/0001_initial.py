# Generated by Django 3.1.6 on 2021-12-05 00:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitudes', '0004_auto_20211204_1747'),
        ('usuarios', '0002_auto_20211205_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automovil', models.CharField(max_length=35, verbose_name='Automóvil')),
            ],
            options={
                'verbose_name': 'Automóvil',
                'verbose_name_plural': 'Tipos de automóvil',
            },
        ),
        migrations.CreateModel(
            name='CasaEs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casa_es', models.CharField(max_length=35, verbose_name='Su casa es')),
            ],
            options={
                'verbose_name': 'Su casa es',
                'verbose_name_plural': 'Su casa es',
            },
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discapacidad', models.CharField(max_length=20, verbose_name='Discapacidad')),
            ],
            options={
                'verbose_name': 'Discpacidad',
                'verbose_name_plural': 'Discapacidades',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolaridad', models.CharField(max_length=20, verbose_name='Grado de estudio')),
            ],
            options={
                'verbose_name': 'Grado de estudio',
                'verbose_name_plural': 'Grados de estudios',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_civil', models.CharField(max_length=20, verbose_name='Estado civil')),
            ],
            options={
                'verbose_name': 'Estado civil',
                'verbose_name_plural': 'Estados civiles',
            },
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=35, verbose_name='Ocupación')),
            ],
            options={
                'verbose_name': 'Ocupación',
                'verbose_name_plural': 'Ocupaciones',
            },
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.CharField(max_length=20, verbose_name='Piso')),
            ],
            options={
                'verbose_name': 'Tipo de piso',
                'verbose_name_plural': 'Tipos de piso',
            },
        ),
        migrations.CreateModel(
            name='ServicioSalud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=35, verbose_name='Cuenta con servicio de')),
            ],
            options={
                'verbose_name': 'Servicio de salud',
                'verbose_name_plural': 'Servicios de salud',
            },
        ),
        migrations.CreateModel(
            name='Techo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techo', models.CharField(max_length=35, verbose_name='Techo')),
            ],
            options={
                'verbose_name': 'Tipo de techo',
                'verbose_name_plural': 'Tipos de techo',
            },
        ),
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_combustible', models.CharField(max_length=35, verbose_name='Tipo de combustible')),
            ],
            options={
                'verbose_name': 'Tipo de combustible',
                'verbose_name_plural': 'Tipos de combustible',
            },
        ),
        migrations.CreateModel(
            name='EstudioSocioeconomico',
            fields=[
                ('folio', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Folio')),
                ('fecha_actual', models.DateField(verbose_name='Fecha')),
                ('credencial', models.FileField(upload_to='credenciales_estudio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf'], message='Sólo se permiten imágenes PNG, JPG, JPEG o PDF.')], verbose_name='Credencial INE/IFE')),
                ('comprobante_domicilio', models.FileField(upload_to='comprobantes/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf'], message='Sólo se permiten imágenes PNG, JPG, JPEG o PDF.')], verbose_name='Comprobante de domicilio')),
                ('calle', models.CharField(max_length=40, verbose_name='Calle')),
                ('numero', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número')),
                ('colonia', models.CharField(max_length=35, verbose_name='Colonia')),
                ('codigo_postal', models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[0-9]*$', 'Sólo se permiten números.')], verbose_name='Código Postal')),
                ('entre_calles', models.CharField(blank=True, max_length=60, null=True, verbose_name='Entre calle y calle')),
                ('telefono', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[0-9]*$', 'Sólo se permiten números.')], verbose_name='Teléfono')),
                ('jefe_familia', models.BooleanField(default=False, verbose_name='¿Es jefe de familia?')),
                ('una_planta', models.BooleanField(default=False, verbose_name='1 Planta')),
                ('dos_planta', models.BooleanField(default=False, verbose_name='2 Planta')),
                ('tres_planta', models.BooleanField(default=False, verbose_name='3 Planta o más')),
                ('sala_comedor', models.BooleanField(default=False, verbose_name='Sala/comedor')),
                ('cocina', models.BooleanField(default=False, verbose_name='Cocina')),
                ('patio', models.BooleanField(default=False, verbose_name='Patio')),
                ('cochera', models.BooleanField(default=False, verbose_name='Cochera')),
                ('numero_recamaras', models.IntegerField(verbose_name='Número de recamaras')),
                ('numero_banios', models.IntegerField(verbose_name='Número de baños')),
                ('otros_caracteristicas_casa', models.CharField(max_length=60, verbose_name='Otro')),
                ('casa_energia', models.BooleanField(default=False, verbose_name='Energía Eléctrica')),
                ('casa_drenaje', models.BooleanField(default=False, verbose_name='Drenaje')),
                ('casa_potable', models.BooleanField(default=False, verbose_name='Agua Potable')),
                ('casa_gas', models.BooleanField(default=False, verbose_name='Instalación Gas')),
                ('casa_lavadora', models.BooleanField(default=False, verbose_name='Lavadora de ropa')),
                ('casa_refrigerador', models.BooleanField(default=False, verbose_name='Refrigerador')),
                ('casa_tv', models.BooleanField(default=False, verbose_name='T.V.')),
                ('casa_tel_fijo', models.BooleanField(default=False, verbose_name='Teléfono fijo')),
                ('casa_tel_celular', models.BooleanField(default=False, verbose_name='Teléfono celular')),
                ('casa_microondas', models.BooleanField(default=False, verbose_name='Horno de microondas')),
                ('casa_radio', models.BooleanField(default=False, verbose_name='Radio/Stéreo')),
                ('casa_dvd', models.BooleanField(default=False, verbose_name='DVD')),
                ('casa_computadora', models.BooleanField(default=False, verbose_name='Computadora')),
                ('casa_laptop', models.BooleanField(default=False, verbose_name='Laptop')),
                ('enfermedad_cancer', models.BooleanField(default=False, verbose_name='Cáncer')),
                ('enfermedad_quemaduras', models.BooleanField(default=False, verbose_name='Quemaduras')),
                ('enfermedad_epilepsia', models.BooleanField(default=False, verbose_name='Epilepsia')),
                ('enfermedad_hipertension', models.BooleanField(default=False, verbose_name='Hipertensión')),
                ('enfermedad_presion_baja', models.BooleanField(default=False, verbose_name='Presión baja')),
                ('enfermedad_discapacidad', models.BooleanField(default=False, verbose_name='Discapacidad')),
                ('enfermedad_cardiacos', models.BooleanField(default=False, verbose_name='Cardíacos')),
                ('enfermedad_estrabismo', models.BooleanField(default=False, verbose_name='Estrabismo')),
                ('enfermedad_renales', models.BooleanField(default=False, verbose_name='Renales')),
                ('enfermedad_alergia', models.BooleanField(default=False, verbose_name='Alergías')),
                ('enfermedad_paladar_hendido', models.BooleanField(default=False, verbose_name='Paladar Hendido')),
                ('enfermedad_cardipatias', models.BooleanField(default=False, verbose_name='Cardiopatías')),
                ('enfermedad_diabetes', models.BooleanField(default=False, verbose_name='Diabetes')),
                ('enfermedad_alzhaimer', models.BooleanField(default=False, verbose_name='Alhzaimer')),
                ('enfermedad_otro', models.CharField(max_length=60, verbose_name='otro (Especifique)')),
                ('receta', models.FileField(null=True, upload_to='recetas/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf'], message='Sólo se permiten imágenes PNG, JPG, JPEG o PDF.')], verbose_name='Receta en caso de ser necesario')),
                ('automovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.automovil', verbose_name='Automóvil')),
                ('casa_es', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.casaes', verbose_name='Su casa es')),
                ('discapacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.discapacidad', verbose_name='Discapacidad')),
                ('escolaridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.escolaridad', verbose_name='Escolaridad')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.estado', verbose_name='Estado')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.estadocivil', verbose_name='Estado civil')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.localidad', verbose_name='Localidad')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.municipio', verbose_name='Municipio')),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.ocupacion', verbose_name='Ocupacion')),
                ('piso_es', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.piso', verbose_name='El piso es')),
                ('servicio_salud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.serviciosalud', verbose_name='Ocupacion')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solicitud', verbose_name='Solicitud')),
                ('techo_es', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.techo', verbose_name='El techo es')),
                ('tipo_combustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_socioeconomico.tipocombustible', verbose_name='Tipo de combustible')),
            ],
            options={
                'verbose_name': 'Estudio socioesconomico',
                'verbose_name_plural': 'Estudios socioeconomicos',
            },
        ),
    ]