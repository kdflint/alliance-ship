import logging, requests
from pygithub3 import Github
from django.conf import settings
#from django.contrib.sessions.backends.db import SessionStore
	
def get_user_teams(backend, user, response, details, *args, **kwargs):
	if backend.name == 'github':
		logger = logging.getLogger("alliance")
		#s = SessionStore()
		r = requests.get('https://api.github.com/user/teams?access_token=' + response['access_token'])
		t = ''
		for item in r.json():
			#logger.debug(item['organization']['id'])
			#logger.debug(item['organization']['name'])
			#logger.debug(item['name'])
			t = t + item['name'] + ','
		logger.debug("Ending with " + t)
		#s['test'] = t
		#s.save()
		#logger.debug(s._session_key)
   