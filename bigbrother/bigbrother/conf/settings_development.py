from .settings import *
import os


#
# Standard Django settings.
#
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = 'bigbrother.wsgi.wsgi_development.application'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'bigbrother.db'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Additional Django settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

#
# Django debug toolbar
#
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

#
# Adeweb backend
# use 'bigbrother.adeweb.backends.dummy.API' for testing purposes
#
ADEWEB_API={
    'BACKEND': 'adeweb.backends.dummy.API',
}

# Override settings with local settings.
try:
    from settings_local import *
except ImportError:
    pass
