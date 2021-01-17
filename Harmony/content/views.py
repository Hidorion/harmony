from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Image,Tip
from login.models import Association
from filters.models import Category

def index(request):
    latest_images = Image.objects.filter(approved=True)[:5]
    associations = Association.objects.filter(approved=True)
    tips = Tip.objects.filter(approved=True)
    context = {'latest_images': latest_images , 'associations': associations , 'tips' : tips}
    return render(request, 'content/index.html', context)

def gallery(request):
    gallery = Image.objects.filter(approved=True)
    context = {'gallery': gallery}
    return render(request, 'content/gallery.html', context)


# class IndexView(generic.ListView):
#     """
#     """

#     template_name = "/Harmony/Harmony/templates/content/index.html"
