from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@given(u'selecciono la solicitud a editar')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_solicitud = tabla.find_elements_by_tag_name('tr')[0]
    td_opciones = tr_solicitud.find_elements_by_tag_name('td')[8]
    boton_editar = td_opciones.find_elements_by_tag_name('a')[1]
    boton_editar.click()


@given(u'corrijo el valor del campo "{campo}": "{valor}"')
def step_impl(context, campo, valor):
    context.driver.find_element_by_name(campo).clear()
    context.driver.find_element_by_name(campo).send_keys(valor)

@when(u'presiono el botón "Guardar"')
def step_impl(context):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)
    time.sleep(1)
