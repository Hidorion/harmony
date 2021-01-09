from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'content/index.html')

# class IndexView(generic.ListView):
#     """
#     """

#     template_name = "/Harmony/Harmony/templates/content/index.html"
