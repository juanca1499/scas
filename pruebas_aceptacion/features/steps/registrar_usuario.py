from behave import given, when, then
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time


@given(u'selecciono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_link_text(boton).click()


@given(u'presiono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_id('agregar').click()


@given(u'capturo el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_id('id_first_name').send_keys(nombre)


@given(u'capturo el primer apellido "{primer_apellido}"')
def step_impl(context, primer_apellido):
    context.driver.find_element_by_id('id_last_name').send_keys(primer_apellido)


@given(u'capturo el segundo apellido "{segundo_apellido}"')
def step_impl(context, segundo_apellido):
    context.driver.find_element_by_id('id_segundo_apellido').send_keys(segundo_apellido)


@given(u'capturo la calle "{calle}"')
def step_impl(context, calle):
    context.driver.find_element_by_id('id_calle').send_keys(calle)


@given(u'capturo en el numero "{numero}"')
def step_impl(context, numero):
    context.driver.find_element_by_id('id_numero').send_keys(numero)


@given(u'capturo la colonia "{colonia}"')
def step_impl(context, colonia):
    context.driver.find_element_by_id('id_colonia').send_keys(colonia)


@given(u'capturo el código postal "{codigo_postal}"')
def step_impl(context, codigo_postal):
    context.driver.find_element_by_id('id_codigo_postal').send_keys(codigo_postal)


@given(u'elijo el estado "{estado}"')
def step_impl(context, estado):
    select = Select(context.driver.find_element_by_id('id_estado'))
    select.select_by_visible_text(estado)
    time.sleep(3)


@given(u'elijo el municipio "{municipio}"')
def step_impl(context, municipio):
    select = Select(context.driver.find_element_by_id('id_municipio'))
    select.select_by_visible_text(municipio)
    time.sleep(2)


@given(u'elijo la localidad "{localidad}"')
def step_impl(context, localidad):
    select = Select(context.driver.find_element_by_id('id_localidad'))
    select.select_by_visible_text(localidad)
    time.sleep(2)


@given(u'capturo el correo "{correo}"')
def step_impl(context, correo):
    context.driver.find_element_by_id('id_email').send_keys(correo)


@given(u'capturo el teléfono "{telefono}"')
def step_impl(context, telefono):
    context.driver.find_element_by_id('id_telefono').send_keys(telefono)


@given(u'subo fotografía de mi INE')
def step_impl(context):
    context.driver.find_element_by_id('id_ine').send_keys(r'C:/Users/karlo/Desktop/PruebasArchivos/Cred.pdf')


@given(u'capturo el usuario "{usuario}"')
def step_impl(context, usuario):
    context.driver.find_element_by_id('id_username').send_keys(usuario)


@given(u'capturar la contraseña "{contra}"')
def step_impl(context, contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(2)


@when(u'presiono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_id('submit').send_keys(Keys.ENTER)


@then(u'puedo ver al usuario "{usuario}" en la lista de usuarios.')
def step_impl(context, usuario):
    context.test.assertIn(usuario, context.driver.page_source)


@then(u'puedo ver el mensaje "{mensaje}".')
def step_impl(context, mensaje):
    context.test.assertIn(mensaje, context.driver.page_source)
