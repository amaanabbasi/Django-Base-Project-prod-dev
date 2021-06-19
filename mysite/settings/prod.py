from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False # This should be False.

WSGI_APPLICATION = 'mysite.wsgi.prod.application'

ALLOWED_HOSTS = ['aws-ipv4-ip']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('RDS_DB_NAME'),
        'USER': config('RDS_USERNAME'),
        'PASSWORD': config('RDS_PASSWORD'),
        'HOST': config('RDS_HOSTNAME'),
        'PORT': config('RDS_PORT'),
    }
}


CORS_ORIGIN_WHITELIST = (
    '',
)
