from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from .models import ExtendUser
from .models import Accounts

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class ExtendUserInline(admin.StackedInline):
#     model = ExtendUser
#     can_delete = False
#     verbose_name_plural = 'user'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ExtendUserInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Accounts)