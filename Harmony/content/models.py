from django.db import models
from Harmony.Models.filter import Category, Department
from Harmony.Models.account import Account


class Event(models.Model):
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    department = models.ForeignKey(Department)
    date_start = models.DateField()
    date_end = models.DateField()
    category = models.ManyToManyField(Category)
    account = models.ForeignKey(Account)
    approved = models.BooleanField(null=False , blank=True)

    class Meta:
        managed = True
        db_table = 'event'


class Image(models.Model):
    account = models.ForeignKey(Account)
    url = models.URLField(max_length=-1)
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category)
    posting_date = models.DateField()
    department = models.ForeignKey(Department)
    approved = models.BooleanField(null=False , blank=True)

    class Meta:
        managed = True
        db_table = 'image'


class Tip(models.Model):
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category)
    account = models.ForeignKey(Account)
    approved = models.BooleanField(null=False , blank=True)
    class Meta:
        managed = True
        db_table = 'tip'