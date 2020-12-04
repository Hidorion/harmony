from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'category'


class Country(models.Model):
    country_name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'country'


class Region(models.Model):
    region_name = models.CharField(max_length=-1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'region'

        

class Department(models.Model):
    department_name = models.CharField(max_length=-1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'department'