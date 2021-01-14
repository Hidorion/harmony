from django.urls import path

from . import views

app_name = "content"

urlpatterns = [
    path('', views.index, name='index'),
    path("content/", views.index, name="index"),
    path('content/gallery', views.gallery, name='gallery')
]