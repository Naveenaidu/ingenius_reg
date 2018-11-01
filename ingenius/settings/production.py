import os

from ingenius.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

#ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reg',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': ''
    }
}


STATIC_ROOT = os.environ.get('STATIC_ROOT','None')
