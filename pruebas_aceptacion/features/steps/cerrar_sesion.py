from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time


@given(u'que me encuentro logueado en el sistema')
def step_impl(context):
    context.driver.get(f"{context.url}{'admin/logout'}")
    context.driver.get(context.url)
    context.driver.find_element_by_name('username').send_keys('juca')
    context.driver.find_element_by_name('password').send_keys('juca123')
    context.driver.find_element_by_tag_name('button').click()
    time.sleep(1)


@when(u'selecciono la opción de cerrar sesión')
def step_impl(context):
    context.driver.find_element_by_id('userDropdown').click()
    context.driver.find_element_by_link_text('Cerrar sesión').click()


@then(u'el sistema me dirije a la pantalla de login.')
def step_impl(context):
    assert context.driver.current_url == context.url
