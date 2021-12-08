from behave import given, when, then
import time


@then(u'puedo ver una lista con todos los usuarios registrados en el sistema.')
def step_impl(context):
    context.test.assertIn('Lista de usuarios', context.driver.page_source)
