__author__ = 'yenda'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def load_api():
    try:
        module = getattr(settings, 'ADEWEB_API', {})['BACKEND']
    except:
        raise ImproperlyConfigured('Missing or incorrect Adeweb API settings in ADEWEB_API: "BACKEND".')
    mod = import_module(module)
    cls = getattr(mod, 'API')
    return cls()


class GenericApi(object):
    sessionId = None

    #connects to the adeweb API
    #sets self.sessionId
    def connect(self):
        pass

    def disconnect(self):
        pass

    def set_project(self):
        pass

    def get_resources(self):
        pass

    def get_activities(self):
        pass

    def write_resources(self):
        pass

    def write_activities(self):
        pass


