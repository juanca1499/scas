from typing import KeysView
from behave import given, when, then
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

@given(u'que accedo al login')
def step_impl(context):
    context.driver.get(f"{context.url}{'admin/logout'}")
    context.driver.get(f"{context.url}{''}")


@given(u'capturo usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)


@given(u'presiono ingresar')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div[1]/main/div/div/div/div/div[2]/form/div[3]/button').click()


@given(u'me dirijo a solicitudes')
def step_impl(context):
    context.driver.get(f"{context.url}{'solicitudes'}")
    context.url_solicitudes = context.driver.current_url


@given(u'selecciono visualizar solicitud "{solicitud}"')
def step_impl(context,solicitud):
    path = '/html/body/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[' + solicitud + ']/td[9]/a[1]'
    context.driver.find_element_by_xpath(path).click()

@given(u'selecciono agregar estudio socioeconomico')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div[1]/h1/div/div/div[2]/a').click()


@given(u'capturo en la fecha actual "{fecha}"')
def step_impl(context,fecha):
    context.driver.find_element_by_id('id_fecha_actual').send_keys(fecha)


@given(u'subo un archivo como comprobante de domicilio "{path}"')
def step_impl(context,path):
    archivo = r'%s' % path
    context.driver.find_element_by_id('id_comprobante_domicilio').send_keys(archivo)


@given(u'subo un archivo como la credencial de elector "{path}"')
def step_impl(context,path):
    archivo = r'%s' % path
    context.driver.find_element_by_id('id_credencial').send_keys(archivo)


@given(u'capturo la edad "{edad}"')
def step_impl(context,edad):
    context.driver.find_element_by_id('id_edad').send_keys(edad)


@given(u'capturo el telefono "{telefono}"')
def step_impl(context,telefono):
    context.driver.find_element_by_id('id_telefono').send_keys(telefono)


@given(u'activo la casilla en es cabeza de familia')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_cabeza_familia')
    elemento.send_keys(Keys.SPACE)


@given(u'elijo en ocupación "{ocupacion}"')
def step_impl(context,ocupacion):
    select = Select(context.driver.find_element_by_id('id_ocupacion'))
    select.select_by_visible_text(ocupacion)


@given(u'elijo en escolaridad "{escolaridad}"')
def step_impl(context,escolaridad):
    select = Select(context.driver.find_element_by_id('id_escolaridad'))
    select.select_by_visible_text(escolaridad)


@given(u'elijo en estado civil "{estado_civil}"')
def step_impl(context,estado_civil):
    select = Select(context.driver.find_element_by_id('id_estado_civil'))
    select.select_by_visible_text(estado_civil)


@given(u'elijo en discapacidad "{discapacidad}"')
def step_impl(context,discapacidad):
    select = Select(context.driver.find_element_by_id('id_discapacidad'))
    select.select_by_visible_text(discapacidad)


@given(u'elijo en automovil "{automovil}"')
def step_impl(context,automovil):
    select = Select(context.driver.find_element_by_id('id_automovil'))
    select.select_by_visible_text(automovil)


@given(u'elijo en tipo de combustible "{tipo_combustible}"')
def step_impl(context,tipo_combustible):
    select = Select(context.driver.find_element_by_id('id_tipo_combustible'))
    select.select_by_visible_text(tipo_combustible)

@given(u'capturo calle "{calle}"')
def step_impl(context,calle):
    context.driver.find_element_by_id('id_calle').send_keys(calle)

@given(u'capturo en el numero exterior "{numero_exterior}"')
def step_impl(context,numero_exterior):
    context.driver.find_element_by_id('id_numero_exterior').send_keys(numero_exterior)

@given(u'capturo colonia "{colonia}"')
def step_impl(context,colonia):
    context.driver.find_element_by_id('id_colonia').send_keys(colonia)


@given(u'capturo código postal "{codigo_postal}"')
def step_impl(context,codigo_postal):
    context.driver.find_element_by_id('id_codigo_postal').send_keys(codigo_postal)

@given(u'elijo en estado "{estado}"')
def step_impl(context,estado):
    select = Select(context.driver.find_element_by_id('id_estado'))
    select.select_by_visible_text(estado)
    time.sleep(1)


@given(u'elijo en municipio "{municipio}"')
def step_impl(context,municipio):
    select = Select(context.driver.find_element_by_id('id_municipio'))
    select.select_by_visible_text(municipio)
    time.sleep(1)


@given(u'elijo en localidad "{localidad}"')
def step_impl(context,localidad):
    select = Select(context.driver.find_element_by_id('id_localidad'))
    select.select_by_visible_text(localidad)
    time.sleep(1)


@given(u'activo la casilla en 3 plantas')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_tres_planta')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en sala/comedor')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_sala_comedor')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en cocina')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_cocina')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en cochera')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_cochera')
    elemento.send_keys(Keys.SPACE)


@given(u'capturo el numero de recamaras "{numero_recamaras}"')
def step_impl(context,numero_recamaras):
    context.driver.find_element_by_id('id_numero_recamaras').send_keys(numero_recamaras)


@given(u'capturo el numero de baños "{numero_banios}"')
def step_impl(context,numero_banios):
    context.driver.find_element_by_id('id_numero_banios').send_keys(numero_banios)


@given(u'elijo en el piso es "{piso_es}"')
def step_impl(context,piso_es):
    select = Select(context.driver.find_element_by_id('id_piso_es'))
    select.select_by_visible_text(piso_es)


@given(u'elijo en el techo es "{techo_es}"')
def step_impl(context,techo_es):
    select = Select(context.driver.find_element_by_id('id_techo_es'))
    select.select_by_visible_text(techo_es)


@given(u'elijo en su casa es "{casa_es}"')
def step_impl(context,casa_es):
    select = Select(context.driver.find_element_by_id('id_casa_es'))
    select.select_by_visible_text(casa_es)
    time.sleep(2)

@given(u'activo la casilla en energia electrica')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_energia')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en drenaje')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_drenaje')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en agua potable')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_potable')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en lavadora')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_lavadora')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en radio')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_radio')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en dvd')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_casa_dvd')
    elemento.send_keys(Keys.SPACE)
    time.sleep(2)


@given(u'elijo en servio de salud "{servicio_salud}"')
def step_impl(context,servicio_salud):
    select = Select(context.driver.find_element_by_id('id_servicio_salud'))
    select.select_by_visible_text(servicio_salud)


@given(u'activo la casilla en cancer')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_enfermedad_cancer')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en epilepsia')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_enfermedad_epilepsia')
    elemento.send_keys(Keys.SPACE)


@given(u'activo la casilla en presion baja')
def step_impl(context):
    elemento = context.driver.find_element_by_id('id_enfermedad_presion_baja')
    elemento.send_keys(Keys.SPACE)
    time.sleep(2)
    
@when(u'presiono botón "Agregar"')
def step_impl(context):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)


@then(u'el sistema me muestra "{mensaje}"')
def step_impl(context,mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)
    time.sleep(2)