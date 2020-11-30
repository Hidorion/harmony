from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=-1)
    id_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='id_parent', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'


class Country(models.Model):
    country_name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'country'


class Department(models.Model):
    department_name = models.CharField(max_length=-1)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = True
        db_table = 'department'

class Region(models.Model):
    region_name = models.CharField(max_length=-1)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')

    class Meta:
        managed = True
        db_table = 'region'