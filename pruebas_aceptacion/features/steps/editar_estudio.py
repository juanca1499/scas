from behave import given, when, then
from selenium.webdriver.common.keys import Keys

import time


@given(u'me dirijo a estudios socioeconomicos')
def step_impl(context):
    context.driver.get(f"{context.url}{'estudio-socieconomico'}")
    context.url_solicitudes = context.driver.current_url


@given(u'selecciono editar estudio')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_usuario = tabla.find_elements_by_tag_name('tr')[1]
    td_opciones = tr_usuario.find_elements_by_tag_name('td')[6]
    boton_editar = td_opciones.find_elements_by_tag_name('a')[1]
    boton_editar.click()


@given(u'cambio la colonia por "{colonia}"')
def step_impl(context, colonia):
    context.driver.find_element_by_id('id_colonia').clear()
    context.driver.find_element_by_id('id_colonia').send_keys(colonia)


@when(u'presiono botón "Guardar"')
def step_impl(context):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)
    time.sleep(2)
