
from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time


@given(u'selecciono el usuario a dar de baja')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_usuario = tabla.find_elements_by_tag_name('tr')[1]
    td_opciones = tr_usuario.find_elements_by_tag_name('td')[6]
    boton_desactivar = td_opciones.find_element_by_tag_name('button')
    boton_desactivar.click()
    time.sleep(3)


@when(u'confirmo la acción')
def step_impl(context):
    botones_alerta = context.driver.find_element_by_class_name('swal2-actions')
    boton_confirmar = botones_alerta.find_element_by_tag_name('button')
    boton_confirmar.click()


@then(u'el sistema deberá mostrar el mensaje: "{mensaje}"')
def step_impl(context, mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)
