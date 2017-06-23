DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'northbr6_devwaterwheel',
		'USER': 'alliance',
		'PASSWORD': 'beloved',
		'HOST': '127.0.0.1',
		'PORT': '5432',
    }
}

SECRET_KEY = '-ccj-m$@5h9z$t%+9zq6z$y@s%e9+kapdy^ozt4k^lfvpq)bxm'

# Update value to match GitHub OAuth applications: Client Id
SOCIAL_AUTH_GITHUB_KEY = 'd65f4ff7e0cddcc73352'

# Update value to match GitHub OAuth applications: Client Secret
SOCIAL_AUTH_GITHUB_SECRET = '6fbe9f90498881c31a0d0f1fa2512430a7cc72b8'