# Import base to override settings
from .base import *
import os

# Override Github settings
DEBUG = os.getenv('DEBUG', True)

if os.path.isfile('local.py'):
    from .local import *

