import os

from ingenius.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','13.233.113.196']

#ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reg',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': ''
    }
}


#STATIC_ROOT = os.environ.get('STATIC_ROOT',None)
#STATIC_ROOT = os.path.join(BASE_DIR,"static")
