from settings import *

#
# Standard Django settings.
#

DEBUG = False
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = 'bigbrother.wsgi.wsgi_production.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Memcached cache backend setup.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Caching templates.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# Caching sessions.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Production logging facility.
LOGGING['loggers'].update({
    'bigbrother': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

#
# Raven
#
INSTALLED_APPS = list(INSTALLED_APPS) + [
    'raven.contrib.django.raven_compat',
]
RAVEN_CONFIG = {
    'dsn': 'udp://',
}

#
# django-maintenancemode
#
MAINTENANCE_MODE = True
