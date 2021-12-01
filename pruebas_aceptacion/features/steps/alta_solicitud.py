from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time


@given(u'que accedo a la página de login')
def step_impl(context):
    context.driver.get(f"{context.url}{'admin/logout'}")
    context.driver.get(f"{context.url}{'admin'}")


@given(u'capturo en el usuario "{usuario}" y en la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)
    time.sleep(1)


@given(u'inicio sesión')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(1)


@given(u'me dirijo al dashboard')
def step_impl(context):
    context.driver.get(f"{context.url}{'solicitudes'}")
    context.url_solicitudes = context.driver.current_url


@given(u'selecciono agregar solicitud')
def step_impl(context):
    context.driver.find_element_by_link_text('Agregar solicitud').click()
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


@given(u'capturo "{segundo_ap}" el segundo apellido')
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


@given(u'elijo la opción "{estado_civil}" en estado civil')
def step_impl(context, estado_civil):
    select = Select(context.driver.find_element_by_id('id_estado_civil'))
    select.select_by_visible_text(estado_civil)


@given(u'elijo la opción "{grado_estudios}" en el último grado de estudios')
def step_impl(context, grado_estudios):
    select = Select(context.driver.find_element_by_id(
        'id_ultimo_grado_estudios'))
    select.select_by_visible_text(grado_estudios)


@given(u'elijo la opción "{ocupacion}" en la ocupación')
def step_impl(context, ocupacion):
    select = Select(context.driver.find_element_by_id('id_ocupacion'))
    select.select_by_visible_text(ocupacion)


@given(u'capturo "{correo}" en el correo')
def step_impl(context, correo):
    context.driver.find_element_by_id('id_correo').send_keys(correo)


@given(u'capturo "{resumen}" en el resumen de la solicitud')
def step_impl(context, resumen):
    context.driver.find_element_by_id('id_resumen').send_keys(resumen)


@when(u'presiono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[2]/form/input[2]').click()


@then(u'el sistema me reedirecciona a la lista de solicitudes')
def step_impl(context):
    url_actual = context.driver.current_url
    assert url_actual == context.url_solicitudes


@then(u'el sistema me muestra el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    div_error = context.driver.find_element_by_id('mensaje')
    assert div_error.text == mensaje
