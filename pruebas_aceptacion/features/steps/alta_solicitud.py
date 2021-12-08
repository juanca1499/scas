from behave import given, when, then
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


@given(u'que accedo a la página de login')
def step_impl(context):
    context.driver.get(f"{context.url}{'admin/logout'}")
    context.driver.get(context.url)


@given(u'capturo en el usuario "{usuario}" y en la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)
    time.sleep(1)


@given(u'inicio sesión')
def step_impl(context):
    context.driver.find_element_by_tag_name('button').click()
    time.sleep(1)


@given(u'selecciono el botón "boton"')
def step_impl(context):
    context.driver.find_element_by_link_text('Agregar solicitud').click()
    context.url_solicitudes = context.driver.current_url


@given(u'selecciono agregar solicitud')
def step_impl(context):
    context.driver.find_element_by_link_text('Agregar').click()
    context.url_formulario = context.driver.current_url


@given(u'capturo "{fecha}" en la fecha de la solicitud')
def step_impl(context, fecha):
    context.driver.find_element_by_id('id_fecha').send_keys(fecha)


@given(u'capturo "{nombre}" en el nombre')
def step_impl(context, nombre):
    context.driver.find_element_by_id('id_nombre').send_keys(nombre)


@given(u'capturo "{primer_ap}" en el primer apellido')
def step_impl(context, primer_ap):
    context.driver.find_element_by_id(
        'id_primer_apellido').send_keys(primer_ap)


@given(u'capturo "{segundo_ap}" en el segundo apellido')
def step_impl(context, segundo_ap):
    context.driver.find_element_by_id(
        'id_segundo_apellido').send_keys(segundo_ap)


@given(u'capturo "{calle}" en la calle')
def step_impl(context, calle):
    context.driver.find_element_by_id('id_calle').send_keys(calle)


@given(u'capturo "{numero}" en el número')
def step_impl(context, numero):
    context.driver.find_element_by_id('id_numero').send_keys(numero)


@given(u'capturo "{codigo_postal}" en el código postal')
def step_impl(context, codigo_postal):
    context.driver.find_element_by_id(
        'id_codigo_postal').send_keys(codigo_postal)


@given(u'capturo "{seccion}" en la sección')
def step_impl(context, seccion):
    context.driver.find_element_by_id('id_seccion').send_keys(seccion)


@given(u'capturo "{telefono}" en el teléfono')
def step_impl(context, telefono):
    context.driver.find_element_by_id('id_telefono').send_keys(telefono)


@given(u'capturo "{curp}" en la CURP')
def step_impl(context, curp):
    context.driver.find_element_by_id('id_curp').send_keys(curp)


@given(u'capturo "{lugar_nac}" en el lugar de nacimiento')
def step_impl(context, lugar_nac):
    context.driver.find_element_by_id(
        'id_lugar_nacimiento').send_keys(lugar_nac)


@given(u'capturo "{fecha_nacimiento}" en la fecha de nacimiento')
def step_impl(context, fecha_nacimiento):
    context.driver.find_element_by_id(
        'id_fecha_nacimiento').send_keys(fecha_nacimiento)


@given(u'elijo "{estado}" en el estado')
def step_impl(context, estado):
    select = Select(context.driver.find_element_by_id('id_estado'))
    select.select_by_visible_text(estado)
    time.sleep(1)


@given(u'elijo "{municipio}" en el municipio')
def step_impl(context, municipio):
    select = Select(context.driver.find_element_by_id('id_municipio'))
    select.select_by_visible_text(municipio)
    time.sleep(1)


@given(u'elijo "{localidad}" en la localidad')
def step_impl(context, localidad):
    select = Select(context.driver.find_element_by_id('id_localidad'))
    select.select_by_visible_text(localidad)
    time.sleep(1)


@given(u'elijo "{estatus}" en el estatus')
def step_impl(context, estatus):
    select = Select(context.driver.find_element_by_id('id_estatus'))
    select.select_by_visible_text(estatus)


@given(u'capturo "{correo}" en el correo')
def step_impl(context, correo):
    context.driver.find_element_by_id('id_correo').send_keys(correo)


@given(u'capturo "{resumen}" en el resumen de la solicitud')
def step_impl(context, resumen):
    context.driver.find_element_by_id('id_resumen').send_keys(resumen)


@when(u'presiono el botón "Registrar"')
def step_impl(context):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)
    time.sleep(2)
