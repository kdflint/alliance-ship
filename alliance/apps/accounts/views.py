from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect

def login(request):
    return render_to_response("accounts/login.html",{"user":request.user})

def logged(request):
    return render_to_response("accounts/logged.html",{"user":request.user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")