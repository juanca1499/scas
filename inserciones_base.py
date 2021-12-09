# Creación de grupos con código 
import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','lema.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from usuarios.models import Usuario, Estado, Municipio, Localidad


# Grupos de usuarios
grupo_encuestadores = Group.objects.create(name='Encuestadores')

content_type = ContentType.objects.get_for_model(Usuario)

# Asignación de permisos al grupo de encuestadores
grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='add_solicitud'))
grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='view_solicitud'))
grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='change_solicitud'))

grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='add_estudiosocioeconomico'))
grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='change_estudiosocioeconomico'))
grupo_encuestadores.permissions.add(Permission.objects.get(
    codename='view_estudiosocioeconomico'))

# Estados
zacatecas = Estado.objects.create(nombre='Zacatecas')

# Municipios
zacatecas_mun = Municipio.objects.create(nombre='Zacatecas',
                                         estado=zacatecas)
guadalupe_mun = Municipio.objects.create(nombre='Guadalupe',
                                         estado=zacatecas)
jerez_mun = Municipio.objects.create(nombre='Jerez',
                                     estado=zacatecas)
calera_mun = Municipio.objects.create(nombre='Calera',
                                      estado=zacatecas)

# Localidades
zacatecas_loc = Localidad.objects.create(nombre='Zacatecas',
                                         municipio=zacatecas_mun)
guadalupe_loc = Localidad.objects.create(nombre='Guadalupe',
                                         municipio=guadalupe_mun)
jerez_loc = Localidad.objects.create(nombre='Jerez',
                                     municipio=jerez_mun)
calera_loc = Localidad.objects.create(nombre='Calera',
                                      municipio=calera_mun)

# Super usuario principal
administrador = Usuario.objects.create_superuser(
    first_name = 'Juan Carlos',
    last_name = 'García',
    segundo_apellido = 'Murillo',
    fecha_nacimiento =  '1999-10-14',
    calle = 'Rafael Acuña',
    numero_exterior = 9,
    colonia = 'Artesanos',
    codigo_postal = '99343',
    telefono = '4949428829',
    ine = 'ine.jpg',
    rfc_corto = 'GAMJ991014',
    estado = zacatecas,
    municipio = jerez_mun,
    localidad = jerez_loc,
    username = 'juca',
    password = 'juca123',
    email = 'juca@gmail.com',
    is_superuser = True,
    is_staff = True,
    is_active = True,
)