from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from .models import Image,Tip,ImageForm,TipForm
from login.models import Association, UserData
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

def adding(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        formToAdd = ImageForm()
        formToAlsoAdd = TipForm()
        if request.method == 'POST' :
            formToAdd = ImageForm(request.POST)
            formToAlsoAdd = TipForm(request.POST)
            if formToAdd.is_valid() :
                formToAdd.save()
            elif formToAlsoAdd.is_valid() :
                formToAdd.save()
        else :
            formToAdd = ImageForm(initial={'owner': request.user.id})
            formToAlsoAdd = TipForm(initial={'owner' : request.user.id})
        context = {'formToAdd' : formToAdd , 'formToAlsoAdd' : formToAlsoAdd }
    return render(request, 'content/add_content.html' , context)

def legal(request):
    return render(request, 'menu/legal.html')