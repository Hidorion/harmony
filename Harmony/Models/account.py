from django.db import models
from .filter import Category, Department




class Association(models.Model):
    category = models.ManyToManyField(Category)
    department = models.ForeignKey(Department)
    asso_name = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'

class User(models.Model):
    firstname = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    year_of_birth = models.IntegerField()
    department = models.ForeignKey(Department)
    asso = models.ManyToManyField(Association)

    class Meta:
        managed = True
        db_table = 'user'

class Account(models.Model):
    user = models.ForeignKey(User)
    asso = models.ForeignKey(Association)
    email = models.CharField(max_length=-1)
    password = models.CharField(max_length=-1)
    registration_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'account'