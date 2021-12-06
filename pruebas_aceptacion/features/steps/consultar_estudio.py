from behave import given, when, then
import time


@given(u'selecciono visualizar solicitud')
def step_impl(context):
    tabla = context.driver.find_element_by_tag_name('tbody')
    tr_solicitud = tabla.find_elements_by_tag_name('tr')[1]
    context.solicitud = tr_solicitud.find_elements_by_tag_name('td')[3].get_attribute('innerHTML')
    td_opciones = tr_solicitud.find_elements_by_tag_name('td')[8]
    boton_detalle = td_opciones.find_elements_by_tag_name('a')[0]
    boton_detalle.click()
    
@given(u'selecciono ver estudio socioeconomico')
def step_impl(context):
    context.driver.find_element_by_xpath(
    '/html/body/div/div/div[1]/div/div[1]/h1/div/div/div[2]/a')

@then(u'el sistema deberá mostrar el estudio socioeconomico.')
def step_impl(context):
    context.test.assertIn(context.solicitud, context.driver.page_source)
    