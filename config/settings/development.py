from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'dc73v84vipmvnc',
       'USER': 'gxsgerbfgtmlit',
       'PASSWORD': '75071f7382e62f839a12178d0019ee0828d93e26ce02de9681acccd1bdb1120f',
       'HOST': 'ec2-34-252-152-193.eu-west-1.compute.amazonaws.com',
       'PORT': 5432,
   }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
