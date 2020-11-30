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


class Association(models.Model):
    id_category = models.IntegerField()
    id_department = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department')
    asso_name = models.CharField(max_length=-1)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'

class User(models.Model):
    firstname = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    year_of_birth = models.IntegerField()
    id_department = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department')
    id_asso = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user'