import logging, requests
from pygithub3 import Github
from django.conf import settings
	
def get_user_teams(backend, user, response, details, *args, **kwargs):
	if backend.name == 'github':
		logger = logging.getLogger("alliance")
		r = requests.get('https://api.github.com/user/teams?access_token=' + response['access_token'])
		t = ''
		for item in r.json():
			#logger.debug(item['organization']['name'])
			#logger.debug(item['name'])
			# TODO - if item['organization']['name'] == Northbridge Technology Alliance:
			t = t + '\'' + item['name'] + '\','
		# TODO - if len(t) == 0: 
			# don't let in
			# possibly throw error so that user is redirected to SOCIAL_AUTH_LOGIN_ERROR_URL
			# should show a person to contact in order to be added to a Northbridge team
		details['first_name'] = t[0:30]	
		details['last_name'] = t[30:60]
