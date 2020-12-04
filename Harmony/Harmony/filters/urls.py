from django.urls import path

from . import views

urlpatterns = [
    path('', views.tag, name='tag'),
]