__author__ = 'yenda'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def load_api():
    try:
        module = getattr(settings, 'ADEWEB_API', {})['BACKEND']
    except:
        raise ImproperlyConfigured('Missing or incorrect Adeweb API settings in ADEWEB_API: "BACKEND".')
    mod = import_module(module)
    cls = getattr(mod, 'API')
    return cls()



