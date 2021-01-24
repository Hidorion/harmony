from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from .models import Association, LoginForm
from django.contrib.auth import authenticate, login

def loginView (request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        formToAdd = LoginForm()
        if request.method == 'POST' :
            formToAdd = LoginForm(request.POST)
            if formToAdd.is_valid() :
                login_in(request)
        else :
            formToAdd = LoginForm(initial={'owner': request.user.id})
        context = {'formToAdd' : formToAdd }
    return render(request, 'login/login.html', context)

def login_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        print("no no")