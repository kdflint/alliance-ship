# This file is only a pattern. It is not referenced at runtime.
# It is used during vagrant provisioning to create a local, unsourced settings file,
# which should then be updated with correct values according to install instructions.

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

# TODO - what is this used for and where is it from??
SECRET_KEY = '-ccj-m$@5h9z$t%+9zq6z$y@s%e9+kapdy^ozt4k^lfvpq)abc'

# Update value to match GitHub OAuth applications: Client Id
# This credentials OAuth conversation
SOCIAL_AUTH_GITHUB_KEY = 'd65f4ff7e0cddcc12345'

# Update value to match GitHub OAuth applications: Client Secret
# This credentials OAuth conversation
SOCIAL_AUTH_GITHUB_SECRET = '6fbe9f90498881c31a0d0f1fa2512430a7c12345'