from behave import given, when, then
import time

@then(u'puedo ver una lista con todas las solicitudes capturadas en el sistema.')
def step_impl(context):
    context.test.assertIn('Lista de solicitudes', context.driver.page_source)
    
@then(u'puedo ver una lista con todas las solicitudes que he capturado.')
def step_impl(context):
    context.test.assertIn('Lista de solicitudes', context.driver.page_source)