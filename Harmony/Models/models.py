# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_asso = models.ForeignKey('Association', models.DO_NOTHING, db_column='id_asso', blank=True, null=True)
    email = models.CharField(max_length=-1)
    password = models.CharField(max_length=-1)
    registration_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'account'


class AccountEvent(models.Model):
    id_account = models.ForeignKey('Account', models.DO_NOTHING, db_column='id_account')
    id_event = models.ForeignKey('Event', models.DO_NOTHING, db_column='id_event')

    class Meta:
        managed = True
        db_table = 'account_event'


class AccountTip(models.Model):
    id_account = models.ForeignKey('Account', models.DO_NOTHING, db_column='id_account')
    id_tip = models.ForeignKey('Tip', models.DO_NOTHING, db_column='id_tip')

    class Meta:
        managed = True
        db_table = 'account_tip'


class AssoCategory(models.Model):
    id_asso = models.ForeignKey('Association', models.DO_NOTHING, db_column='id_asso')
    id_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = True
        db_table = 'asso_category'


class Association(models.Model):
    id_category = models.IntegerField()
    id_department = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department')
    asso_name = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'


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


class Event(models.Model):
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department')
    date_start = models.DateField()
    date_end = models.DateField()
    id_category = models.IntegerField()
    id_account = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'event'


class EventCategory(models.Model):
    id_event = models.ForeignKey(Event, models.DO_NOTHING, db_column='id_event')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = True
        db_table = 'event_category'


class Image(models.Model):
    id_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='id_account')
    url = models.CharField(max_length=-1)
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    id_category = models.IntegerField()
    posting_date = models.DateField()
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department')

    class Meta:
        managed = True
        db_table = 'image'


class ImgCategory(models.Model):
    id_image = models.ForeignKey(Image, models.DO_NOTHING, db_column='id_image')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = True
        db_table = 'img_category'


class Region(models.Model):
    region_name = models.CharField(max_length=-1)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')

    class Meta:
        managed = True
        db_table = 'region'


class Tip(models.Model):
    title = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)
    id_category = models.IntegerField()
    id_account = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tip'


class TipCategory(models.Model):
    id_tip = models.ForeignKey(Tip, models.DO_NOTHING, db_column='id_tip')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = True
        db_table = 'tip_category'


class User(models.Model):
    firstname = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    year_of_birth = models.IntegerField()
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department')
    id_asso = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user'


class UserAsso(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    id_asso = models.ForeignKey(Association, models.DO_NOTHING, db_column='id_asso')

    class Meta:
        managed = True
        db_table = 'user_asso'
