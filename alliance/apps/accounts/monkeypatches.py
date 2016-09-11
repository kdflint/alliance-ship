import logging

# https://opensourcehacker.com/2010/08/12/applying-monkey-patches-in-django-middleware-layer/

_original_auth_complete = None

def _patched_auth_complete(self, *args, **kwargs):
    logger = logging.getLogger("alliance")
    #logger.info("hello from _patched_auth_complete")
    """Completes login process, must return user instance"""
    # LEFT OFF - above log message puts out
    # Now, diagnose. Why does following line throw exception?
    #logger.info("Session state = " + self.get_session_state())
    #logger.info("Request state = " + self.get_request_state())
    state = self.validate_state()
    #logger.info("Returned value = " + state)
    #logger.info(self.data)
    self.process_error(self.data)

    response = self.request_access_token(
        self.access_token_url(),
        data=self.auth_complete_params(state),
        headers=self.auth_headers(),
        auth=self.auth_complete_credentials(),
        method=self.ACCESS_TOKEN_METHOD
    )
    #logger.info(response)
    self.process_error(response)
    return self.do_auth(response['access_token'], response=response, *args, **kwargs)

class PatchedOauthAuth(object):

    def process_request(self, request):
        logger = logging.getLogger("alliance")
        logger.debug("Hello from process_request")
        
        #Install monkey-patch on demand.
        #
        #If monkey-patch has not been run in for this process (assuming multiple preforked processes),
        #then do it now.

        from social.backends.github import GithubOAuth2

        global _original_auth_complete, _patched_auth_complete

        #if not _original_auth_complete:
        if False:
            logger.debug("hello from replacing auth_complete with patch")
            # replace one of the class's method with own fixed version
            #_original_auth_complete = GithubOAuth2.auth_complete
            # GithubOAuth2.auth_complete = _patched_auth_complete
        else:
            logger.debug("auth_complete is already populated or patched")
