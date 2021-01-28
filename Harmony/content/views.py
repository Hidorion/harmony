from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.core.paginator import Paginator
#IMPORT DB'S MODELS
from .models import Image,Tip
from login.models import Association, UserData
from filters.models import Category
from .form import ImageForm,TipForm



def index(request):
    latest_images = Image.objects.filter(approved=True)[5:]
    associations = Association.objects.filter(approved=True)
    tips = Tip.objects.filter(approved=True)
    context = {'latest_images': latest_images , 'associations': associations , 'tips' : tips}
    return render(request, 'content/index.html', context)

def gallery(request):
    wholeGallery = Image.objects.filter(approved=True)
    paginator = Paginator(wholeGallery, 5) # Show 5 pics per page.
    page_number = request.GET.get('page') # Get the page sorted
    page_obj = paginator.get_page(page_number) # Get the number of pages
    context = {'wholeGallery': wholeGallery , 'page_obj': page_obj}
    return render(request, 'content/gallery.html', context)

def tips(request):
    listTip = Tip.objects.filter(approved=True)
    paginator = Paginator(listTip, 3) # Show 3 tips per page.
    page_number = request.GET.get('page') # Get the page sorted
    page_obj = paginator.get_page(page_number) # Get the number of pages
    context = {'listTip': listTip , 'page_obj': page_obj}
    return render(request, 'content/tips.html', context)

def adding(request):
    if not request.user.is_authenticated:
        return redirect("/adminature/login/?next=/content/add")
    else:
        formImage = ImageForm(initial={'owner': request.user.id})
        formTips = TipForm(initial={'owner' : request.user.id})
        formSuccess = ""
        if request.method == 'POST' :
            formImage = ImageForm(request.POST)
            formTips = TipForm(request.POST)
            if formImage.is_valid() :
                formImage.save()
                formSuccess = "Partage réussi"
            elif formTips.is_valid() :
                formTips.save()
                formSuccess = "Partage réussi"
            else :
                formSuccess = "Il y a eu une erreur, il faut recommencer désolé"
                return redirect('/content/add')
        context = {'formImage' : formImage , 'formTips' : formTips, 'formSuccess' : formSuccess} 
        
    return render(request, 'content/add_content.html' , context)

def legal(request):
    return render(request, 'menu/legal.html')
