from django.contrib import admin
from .models import UserData, Association
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin
# Register your models here.

class UserDataInline(admin.StackedInline):
    model=UserData
    can_delete = False
    verbose_name = "Utilisateur"

class UserAdmin(BaseAdmin):
    inlines=(UserDataInline,)

admin.site.register(UserData)
admin.site.register(Association)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)