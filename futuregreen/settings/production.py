from futuregreen.settings.common import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
        'NAME': 'futuregreen', # Or path to database file if using sqlite3.
        'USER': 'futuregreen', # Not used with sqlite3.
        'PASSWORD': 'b875d5c1', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)

