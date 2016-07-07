import logging, requests
from pygithub3 import Github
from django.conf import settings

	
def get_user_teams(backend, user, response, details, *args, **kwargs):
	if backend.name == 'github':
		logger = logging.getLogger("alliance")
		logger.debug("Hello from teams pipeline")
		logger.debug("Github user is" + user.username)
		r = requests.get('https://api.github.com/user/teams?access_token=' + response['access_token'])
		#logger.debug(r.json())
		details['teams_list'] = ''
		logger.debug(details)
		for item in r.json():
			logger.debug(item['organization']['id'])
			logger.debug(item['organization']['name'])
			logger.debug(item['name'])
			details['teams_list'] = details['teams_list'] + item['name'] + ','
			# LEFT OFF
			# For every Northbridge team, add to teams array that is being read in 

    