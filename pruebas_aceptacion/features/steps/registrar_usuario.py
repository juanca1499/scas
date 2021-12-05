from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time


@given(u'selecciono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_link_text(boton).click()


@given(u'presiono el botón "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_id('agregar').click()


@given(u'capturo el nombre "{nombre}"')
def step_impl(context, nombre):
    pass


@given(u'capturo el primer apellido "{primer_apellido}"')
def step_impl(context, primer_apellido):
    pass


@given(u'capturo el segundo apellido "{segundo_apellido}"')
def step_impl(context, segundo_apellido):
    pass


@given(u'capturo la calle "{calle}"')
def step_impl(context, calle):
    pass


@given(u'capturo en el numero "{numero}"')
def step_impl(context, numero):
    pass


@given(u'capturo la colonia "{colonia}"')
def step_impl(context, colonia):
    pass


@given(u'capturo el código postal "{codigo_postal}"')
def step_impl(context, codigo_postal):
    pass


@given(u'elijo la localidad "{localidad}"')
def step_impl(context, localidad):
    pass


@given(u'elijo el municipio "{municipio}"')
def step_impl(context, municipio):
    pass


@given(u'elijo el estado "{estado}"')
def step_impl(context, estado):
    pass


@given(u'capturo el correo "{correo}"')
def step_impl(context, correo):
    pass


@given(u'capturo el teléfono "{4921736547}"')
def step_impl(context, telefono):
    pass


@given(u'subo fotografía de mi INE')
def step_impl(context):
    pass


@given(u'capturo el usuario "{usuario}"')
def step_impl(context, usuario):
    pass


@given(u'capturar la contraseña "{contra}"')
def step_impl(context, contra):
    pass


@then(u'puedo ver al usuario "{usuario}" en la lista de usuarios.')
def step_impl(context, usuario):
    pass


@then(u'puedo ver el mensaje "{mensaje}".')
def step_impl(context):
    pass