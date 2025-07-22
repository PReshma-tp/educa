from .base import *

DEBUG = False

ADMINS = (
    ('reshma', 'reshma@test.in'),
 )

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
   }
}

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True