# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from unittest import TestCase


@fixture
def browser_chrome(context):
    context.driver = Chrome()
    context.url = 'http://192.168.33.10:8000/'
    context.test = TestCase()
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after_all() hook
