from django.shortcuts import render
from django.http import HttpResponse


def media(request):
    return HttpResponse("Cela affiche le continue")