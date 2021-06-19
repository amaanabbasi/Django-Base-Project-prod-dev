from .base import *


SECRET_KEY = '%@e^$*-f@hd*)a3bt2^x^-@13#prwetdnax3u*^73@^z#123dfd3^'

DEBUG = True

WSGI_APPLICATION = 'mysite.wsgi.dev.application'

ALLOWED_HOSTS = ["*"]
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

