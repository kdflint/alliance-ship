import dj_database_url
import os
import logging.config
from os.path import abspath, basename, dirname, join, normpath
from os import listdir
from sys import path

SESSION_COOKIE_SECURE = os.getenv('ALLIANCE_SESSION_COOKIE_SECURE', 'False')

SESSION_COOKIE_SECURE = 'True'
SESSION_COOKIE_HTTPONLY = 'True'
CSRF_COOKIE_SECURE = 'True'
CSRF_COOKIE_HTTPONLY = 'True'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = 'True'
LOGIN_ERROR_URL = '/logged/'

GITHUB_SOCIAL_AUTH_RAISE_EXCEPTIONS = 'True'
SOCIAL_AUTH_RAISE_EXCEPTIONS = 'True'
RAISE_EXCEPTIONS = 'True'
DEBUG = 'True'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            #'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            #'stream': 'sys.stdout'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'alliance': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}


