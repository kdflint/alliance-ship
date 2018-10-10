import os
from os.path import abspath, basename, dirname, join, normpath
from os import listdir
from sys import path

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'northbr6_devwaterwheel',
		'USER': 'alliance',
		'PASSWORD': 'beloved',
		'HOST': '127.0.0.1',
		'PORT': '5432',
    }
}

# TODO - what is this used for and where is it from?
SECRET_KEY = '-ccj-m$@5h9z$t%+9zq6z$y@s%e9+kapdy^ozt4k^lfvpq)abc'

# This credentials OAuth conversation
SOCIAL_AUTH_GITHUB_KEY = 'd65f4ff7e0cddcc12345'

# This credentials OAuth conversation
SOCIAL_AUTH_GITHUB_SECRET = '6fbe9f90498881c31a0d0f1fa2512430a7c12345'

#For github api access
GITHUB_WEBHOOK_SECRET = 'n0rthbr1dge'
GITHUB_OWNER='NorthBridge'
GITHUB_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# GITHUB_TOKEN : Use your generated github personal access token

################################################################################
# Path configuration
################################################################################

# Absolute path of the config directory
CONFIG_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ )))

# Absolute filesystem path to the django repo directory
DJANGO_ROOT = dirname(CONFIG_ROOT)

# Absolute filesystem path to the project directory
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Path to the project parent directory
BASE_DIR = os.path.dirname(PROJECT_ROOT)

# Logging folder
LOG_FOLDER = os.path.join(BASE_DIR, 'logs')

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
        'console':{
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_FOLDER, 'alliance.log'),
            'when' : 'W1', #new log every Tuesday
            'interval' : 1,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console', 'file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'alliance': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
}