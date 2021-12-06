from behave import given, when, then
from selenium.webdriver.common.keys import Keys

import time


@given(u'selecciono el usuario a modificar')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_usuario = tabla.find_elements_by_tag_name('tr')[1]
    td_opciones = tr_usuario.find_elements_by_tag_name('td')[6]
    boton_editar = td_opciones.find_elements_by_tag_name('a')[1]
    boton_editar.click()
    time.sleep(3)


@given(u'cambio el primer apellido por "{apellido}"')
def step_impl(context, apellido):
    context.driver.find_element_by_id('id_last_name').clear()
    context.driver.find_element_by_id('id_last_name').send_keys(apellido)


@given(u'cambio el código postal por "{codigo}"')
def step_impl(context, codigo):
    context.driver.find_element_by_id('id_codigo_postal').clear()
    context.driver.find_element_by_id('id_codigo_postal').send_keys(codigo)


@when(u'presiono el botón guardar')
def step_impl(context):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)


@then(u'el sistema me mostrará el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)
