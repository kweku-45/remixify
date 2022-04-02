from .base_settings import *
from decouple import config

DEBUG = True

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': config('DB_NAME'),

        'USER': config('DB_USER'),

        'PASSWORD': config('DB_PASSWORD'),

        'HOST': config('DB_HOST'),

        'PORT': config('DB_PORT'),

    }

}


ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "django-db"