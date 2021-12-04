from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time


@given(u'que accedo al sistema')
def step_impl(context):
    context.driver.get(f"{context.url}{'admin/logout'}")
    context.driver.get(context.url)


@given(u'me dirijo a la pantalla de login')
def step_impl(context):
    context.driver.get(f"{context.url}{'login'}")


@given(u'capturo el usuario "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)
    

@given(u'capturo el usuario dado de baja "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)


@when(u'presiono el botón de inicio de sesión')
def step_impl(context):
    context.driver.find_element_by_id('ingresar').click()
    time.sleep(1)


@then(u'el sistema me dirige a la página donde se muestran las solicitudes de apoyos que se han realizado.')
def step_impl(context):
    assert context.driver.current_url == '/solicitudes'
    

@then(u'el sistema me muestra el mensaje {mensaje}')
def step_impl(context, mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)