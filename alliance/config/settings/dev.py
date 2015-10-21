#############################################################################################################
# This settings file is purposed for our centralized dev environment installed at alliance-dev.herokuapp.com
# If these configurations do not suit your environment, use a local.py settings file 
# Do not modify these configurations to suit any environment except the one at alliance-dev.herokuapp.com
#############################################################################################################

# Import base to override settings
from .base import *
import os

DEBUG = os.getenv('DEBUG', True)

if os.path.isfile('local.py'):
    from .local import *
