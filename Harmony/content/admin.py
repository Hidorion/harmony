from django.contrib import admin
from .models import Image, Tip
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin
# Register your models here.

class ImagesInline(admin.StackedInline):
    model=Image
    can_delete = False
    verbose_name = "Images"

class UserAdmin(BaseAdmin):
    inlines=(ImagesInline,)

admin.site.register(Image)
admin.site.register(Tip)