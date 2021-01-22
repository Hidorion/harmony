from django.urls import path

from . import views

app_name = "content"

urlpatterns = [
    path('', views.index, name='index'),
    path("content/", views.index, name="index"),
    path('gallery/', views.gallery, name='gallery'),
    path("legal/", views.legal, name="legal"),
    path('content/add', views.adding, name='adding'),
]