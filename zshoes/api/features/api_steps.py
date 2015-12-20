from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import eq_

from zshoes.stores.models import Store

import base64


@before.all
def set_browser():
    world.browser = Client()
    Store.objects.create(id=1, name='Store 1')


@step(r'I authenticates as "(.*)" / "(.*)"')
def authenticate(step, user, password):
    world.auth_headers = {
        'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(
            '{0}:{1}'.format(user, password)),
    }


@step(r'I access the url "(.*)"')
def access_url(step, url):
    auth_headers = {}
    if hasattr(world, 'auth_headers'):
        auth_headers = world.auth_headers
    response = world.browser.get(url, **auth_headers)
    world.response = response
    world.dom = html.fromstring(response.content)
    world.status_code = int(response.status_code)
    world.data = world.response.json()


@step(r'I get status code (.*)')
def see_header(step, status_code):
    eq_(world.status_code, int(status_code))


@step(r'I get error message "(.*)"')
def error_message(step, message):
    eq_(message, world.data['error_msg'])
