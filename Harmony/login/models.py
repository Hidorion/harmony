from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
    asso = models.ManyToManyField('login.Association', blank=True,null=True )

    def __str__(self):
        """
        """

        return f"{self.user}"


    class Meta:
        """
        """

        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

class Association(models.Model):
    category = models.ManyToManyField('filters.Category')
    department = models.ForeignKey('filters.Department',on_delete=models.CASCADE)
    asso_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'association'
