from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect

def logged(request):
    return render(request,"accounts/logged.html",{"user":request.user})
    	
def logout(request):
		auth.logout(request)
		return HttpResponseRedirect("/login")