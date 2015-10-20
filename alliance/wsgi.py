"""
WSGI config for alliance on Heroku.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application  

# This accomodates gunicorn pathing on Heroku
# http://stackoverflow.com/questions/11660627/python-app-import-error-in-django-with-wsgi-gunicorn
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alliance.settings")   
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alliance.config.settings.base")   

 
from dj_static import Cling      

application = Cling(get_wsgi_application())
#application = get_wsgi_application()

