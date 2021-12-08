from behave import given, when, then
import time


@when(u'selecciono el usuario que quiero consultar')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_usuario = tabla.find_elements_by_tag_name('tr')[1]
    context.usuario = tr_usuario.find_elements_by_tag_name(
        'td')[3].get_attribute('innerHTML')
    td_opciones = tr_usuario.find_elements_by_tag_name('td')[6]
    boton_detalle = td_opciones.find_elements_by_tag_name('a')[0]
    boton_detalle.click()
    time.sleep(3)


@then(u'el sistema deberá mostrar los datos del usuario seleccionado.')
def step_impl(context):
    context.test.assertIn(context.usuario, context.driver.page_source)
