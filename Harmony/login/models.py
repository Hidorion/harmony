from django.db import models

class Association(models.Model):
    category = models.ManyToManyField('filters.Category')
    department = models.ForeignKey('filters.Department',on_delete=models.CASCADE)
    asso_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'

class User(models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
    asso = models.ManyToManyField(Association)

    class Meta:
        managed = True
        db_table = 'user'

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asso = models.ForeignKey(Association, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    registration_date = models.DateField() 

    class Meta:
        managed = True
        db_table = 'account'