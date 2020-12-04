from django.shortcuts import render
from django.http import HttpResponse


def tag(request):
    return HttpResponse("Cela affiche les tags")