from django.db import models
from ckeditor.fields import RichTextField
from django import forms
from datetime import *
from login.models import UserData
from django.shortcuts import render
from django.contrib.auth.models import User
# class Event(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=1000)
#     department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
#     date_start = models.DateField()
#     date_end = models.DateField()
#     category = models.ManyToManyField('filters.Category')
#     account = models.ForeignKey('login.Account', on_delete=models.CASCADE)
#     approved = models.BooleanField(null=False , blank=True)

#     class Meta:
#         managed = True
#         db_table = 'event'
# Due to the current sanitary situation, I have decided to postpone the addition of events for now.

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=1000)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    category = models.ManyToManyField('filters.Category')
    posting_date = models.DateField(default=datetime.now)
    department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False , blank=True)

    def __str__(self):
        """
        """
        return f"{self.title},{self.approved}"

    class Meta:
        managed = True
        db_table = 'image'


class Tip(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category = models.ManyToManyField('filters.Category')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(null=False , blank=True)
    content = RichTextField()

    def __str__(self):
        """
        """
        return f"{self.title},{self.approved}"

    class Meta:
        managed = True
        db_table = 'tip'
