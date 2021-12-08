from behave import given, when, then
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


@given(u'selecciono la solicitud que quiero consultar')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_solicitud = tabla.find_elements_by_tag_name('tr')[0]
    context.solicitud = tr_solicitud.find_elements_by_tag_name(
        'td')[3].get_attribute('innerHTML')
    td_opciones = tr_solicitud.find_elements_by_tag_name('td')[8]
    boton_editar = td_opciones.find_elements_by_tag_name('a')[0]
    context.boton_editar = boton_editar


@when(u'presiono el botón Ver detalles')
def step_impl(context):
    context.boton_editar.click()
    time.sleep(1)


@then(u'el sistema deberá mostrar los datos de la solicitud seleccionada.')
def step_impl(context):
    context.test.assertIn(context.solicitud, context.driver.page_source)
