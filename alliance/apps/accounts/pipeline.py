import logging, requests
from pygithub3 import Github
from django.conf import settings
	
def get_user_teams(backend, user, response, details, *args, **kwargs):
	if backend.name == 'github':
		logger = logging.getLogger("alliance")
		# https://developer.github.com/v3/orgs/teams/#list-teams
		r = requests.get('https://api.github.com/user/teams?access_token=' + response['access_token'])
		t = ''
		c = 0
		for item in r.json():
			if item['organization']['name'] == "Northbridge Technology Alliance":
				t = t + item['name'] + ','
				c += 1
		# This is terrible.
		# We overload the user details fields with information about the authorization
		# We should either be adding the teams list to the session or using our own User model
		# Also, can we impact the auth flow from here? Now we are depending on the success view for
		# authorization behavior. Maybe that's ok. Maybe better way. See index.py
		logger.info("Pipeline identified %d teams for github user %s", c, user.username)
		logger.debug(t)
		if len(t) == 0: 
			details['teams'] = 'unauthorized'
			backend.strategy.session_set('gh_teams', 'unauthorized')
		else:
			details['teams'] = t	
			backend.strategy.session_set('gh_teams', t)
