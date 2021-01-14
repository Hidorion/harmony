from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('filters.Department', on_delete=models.CASCADE)
    asso = models.ManyToManyField('login.Association', blank=True )

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
    logo = models.URLField(max_length=1000, null="img/Harmony.png")
    name = models.CharField(max_length=100)
    category = models.ManyToManyField('filters.Category')
    department = models.ForeignKey('filters.Department',on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254, blank=True)
    website = models.URLField(max_length=1000)
    approved = models.BooleanField(null=False , blank=True)

    class Meta:
        managed = True
        db_table = 'association'

    def __str__(self):
        """
        """

        return f"{self.name}"
