from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
    asso = models.ManyToManyField('login.Association')

class Association(models.Model):
    category = models.ManyToManyField('filters.Category')
    department = models.ForeignKey('filters.Department',on_delete=models.CASCADE)
    asso_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'
