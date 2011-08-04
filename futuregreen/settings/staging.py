from futuregreen.settings.base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
        'NAME': 'futuregreen_stage', # Or path to database file if using sqlite3.
        'USER': 'futuregreen_stage', # Not used with sqlite3.
        'PASSWORD': '401a22bc', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)