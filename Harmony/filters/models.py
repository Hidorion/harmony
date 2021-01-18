from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',
        on_delete=models.CASCADE,  
        null=True, 
        blank=True, )

    def __str__(self):
        """
        """
        return f"{self.category_name}"


        
    class Meta:
        managed = True
        db_table = 'category'
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    
    def __str__(self):
        """
        """
        return f"{self.country_name}"
    
    class Meta:
        managed = True
        db_table = 'country'
        verbose_name = "Pays"
        verbose_name_plural = "Pays"    


class Region(models.Model):
    region_name = models.CharField(max_length=50)
    region_code = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        """
        return f"{self.region_name}"

    class Meta:
        managed = True
        db_table = 'region'
        verbose_name = "Région"
        verbose_name_plural = "Régions"

        

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_code = models.CharField(default="0" , max_length=6)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        """
        return f"{self.department_name}"
    
    class Meta:
        managed = True
        ordering = ["department_code"]
        db_table = 'department'
        verbose_name = "Departement"
        verbose_name_plural = "Departements"