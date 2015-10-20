"""
Django settings for alliance project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
#import sys
#import logging.config

#LOGGING_CONFIG = None

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#CORE_PROJECT_DIR = os.path.join(BASE_DIR, 'alliance/core')

#logging.config.fileConfig(os.path.join(CORE_PROJECT_DIR, 'logging.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '-ccj-m$@5h9z$t%+9zq6z$y@s%e9+kapdy^ozt4k^lfvpq)bxm'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

# Application definition

# This accomodates gunicorn pathing on Heroku
# http://stackoverflow.com/questions/11660627/python-app-import-error-in-django-with-wsgi-gunicorn
#sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

#INSTALLED_APPS = (
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'alliance.core',
#    'alliance.apps.backlog',
#    'alliance.apps.accounts',
#    'apps.shared'
#)

#MIDDLEWARE_CLASSES = (
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.security.SecurityMiddleware',
#)

#ROOT_URLCONF = 'alliance.config.urls'


#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # modified to support gunicorn on heroku - don't completely understand yet
#        'DIRS': [os.path.join(BASE_DIR, 'alliance/apps/shared/templates')],
#       'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.debug',
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]


WSGI_APPLICATION = 'alliance.config.wsgi.application'
LOGIN_REDIRECT_URL = 'index'
SESSION_COOKIE_AGE = 10 * 60  # 10 minutes

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'CST6CDT'

#USE_I18N = True

#USE_L10N = True

#USE_TZ = True


#from email_settings import *

# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
TMP_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(TMP_DIR, 'static'),
)
