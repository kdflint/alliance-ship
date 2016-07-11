from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger("alliance")

#def login(request):
#		logger.debug("hello from login view def")
#		return render_to_response("accounts/login.html",{"user":request.user})

def logged(request):
		#logger.debug(item['organization']['id'])
    return render_to_response("accounts/logged.html",{"user":request.user})

def logout(request):
		logger.debug("hello from logout view def")
		auth.logout(request)
		return HttpResponseRedirect("/login")