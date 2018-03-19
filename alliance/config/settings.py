"""
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
import logging.config
from os.path import abspath, basename, dirname, join, normpath
from os import listdir
from sys import path

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

# Project name
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Project folder
PROJECT_FOLDER = basename(PROJECT_ROOT)

# Project domain TODO verify what the project domain should actually be
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

CORE_PROJECT_DIR = os.path.join(PROJECT_ROOT, 'core')

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)

################################################################################
# Static assets configuration
################################################################################

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

################################################################################
# Email configuration
################################################################################

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('SMTP_SERVER')
EMAIL_HOST_USER = os.getenv('SMTP_USER')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_PORT = os.getenv('SMTP_PORT')
EMAIL_RECIPIENT_LIST = os.getenv('SMTP_RECIPIENT_LIST')
EMAIL_SUBJECT_PREFIX = '[%s]' % PROJECT_NAME

################################################################################
# Logging configuration
################################################################################

#LOGGING_CONFIG = None

#logging.config.fileConfig(os.path.join(CORE_PROJECT_DIR, 'logging.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

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


################################################################################
# Security and Debug configuraiton
################################################################################

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)


################################################################################
# Application Configuration
################################################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
   'social.apps.django_app.default',
)

PROJECT_APPS = (
    'apps.shared',
    'apps.backlog',
    'apps.accounts',
)

EXTENSION_APPS = (
    'django_extensions',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS

################################################################################
# Middleware Configuration
################################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'apps.accounts.monkeypatches.PatchedOauthAuth',
)

AUTHENTICATION_BACKENDS = (
		'social.backends.github.GithubOAuth2',
		'django.contrib.auth.backends.ModelBackend',
)

################################################################################
# Template Configuration
################################################################################

def template_folder_paths(app):
    """
    This method is able to get a namespace and transforms it into a normalized
    string with a template path. For example, 'app.google' will return ['app',
    'google'].
    """
    normalized_app = app.split('.') + ['templates']
    return normpath(join(PROJECT_ROOT, *normalized_app))

PROJECT_APP_TEMPLATES = [template_folder_paths(app) for app in PROJECT_APPS]
BASE_TEMPLATES = [normpath(join(PROJECT_ROOT, 'core', 'templates'))]
EXTENSION_TEMPLATES = [normpath(join(PROJECT_ROOT, 'extensions', 'templates'))]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_APP_TEMPLATES + BASE_TEMPLATES + EXTENSION_TEMPLATES,
        'APP_DIRS': True,  # TODO
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
    						'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]


################################################################################
# Database Configuration
################################################################################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = { 'default': dj_database_url.config() }


################################################################################
# Login Configuration
################################################################################


# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
#LOGIN_REDIRECT_URL = 'index'
#LOGIN_REDIRECT_URL = 'http://google.com'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# LOGIN_URL = '/login/'

# https://docs.djangoproject.com/en/dev/ref/settings/#logout-url
# LOGOUT_URL = '/logout/'

SOCIAL_AUTH_LOGIN_URL = '/login/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'backlogs'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/logged/'
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'apps.accounts.pipeline.get_user_teams',
    'social.pipeline.user.user_details',
)

GITHUB_SOCIAL_AUTH_RAISE_EXCEPTIONS = 'True'
SOCIAL_AUTH_RAISE_EXCEPTIONS = 'True'
RAISE_EXCEPTIONS = 'True'
DEBUG = 'True'
LOGIN_ERROR_URL = '/logged/'
FIELDS_STORED_IN_SESSION = ['gh_teams']


################################################################################
# Github API configuration
################################################################################

GITHUB_OWNER = os.getenv('ALLIANCE_GITHUB_OWNER')
GITHUB_TOKEN = os.getenv('ALLIANCE_GITHUB_TOKEN')
GITHUB_WEBHOOK_SECRET = os.getenv('ALLIANCE_GITHUB_WEBHOOK_SECRET')
SOCIAL_AUTH_GITHUB_KEY = os.getenv('ALLIANCE_OAUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('ALLIANCE_OAUTH_GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['read:org']

################################################################################
# Miscellaneous configuration
################################################################################

ROOT_URLCONF = 'config.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SESSION_COOKIE_AGE = 60 * 60  # 60 minutes
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
SOCIAL_AUTH_URL_NAMESPACE = 'social'


################################################################################
# Custom configuration
################################################################################

# Look to see if there is a `local.py` file in the `config` folder, if so, load
# it up and override all the things. We do NOT use these settings if the
# `ALLIANCE_CUSTOM_SETTINGS` are set to False.
has_local_settings = os.path.exists(os.path.join(CONFIG_ROOT,
                                                 'local_settings.py'))
use_custom_settings = os.getenv('ALLIANCE_CUSTOM_SETTINGS', 'True')

if has_local_settings and use_custom_settings == 'True':
    print('Applying local settings overrides (from local_settings.py).')
    from .local_settings import *
