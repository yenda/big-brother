__author__ = 'yenda'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def load_api():
    try:
        module, attr = getattr(settings, 'ADEWEB_API', {})['BACKEND'].rsplit('.', 1)
    except:
        raise ImproperlyConfigured('Missing or incorrect Adeweb API settings in ADEWEB_API: "BACKEND".')
    mod = import_module(module)
    cls = getattr(mod, attr)
    return cls()



