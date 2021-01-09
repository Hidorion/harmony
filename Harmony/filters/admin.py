from django.contrib import admin
from .models import Category,Department,Region,Country
# Register your models here.

admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Region)
admin.site.register(Country)