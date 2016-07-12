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
			#logger.debug(item['organization']['id'])
			#logger.debug(item['name'])
			if item['organization']['name'] == "Northbridge Technology Alliance":
				t = t + item['name'] + ','
		# This is terrible.
		# We overload the user details fields with information about the authentication
		# We should either be adding the teams list to the session or using our own User model
		# Also, can we impact the auth flow from here? Now we are depending on the success view for
		# authorization behavior. Maybe that's ok. Maybe better way. See index.py
		if len(t) == 0: 
			details['first_name'] = 'unauthorized'
		else:
			details['first_name'] = t[0:30]	
			details['last_name'] = t[30:60]
