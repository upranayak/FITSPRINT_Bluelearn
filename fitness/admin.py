from django.contrib import admin
from .models.user import User


class AdminUser(admin.ModelAdmin):
    list_display = ['username']


# Register your models here.

admin.site.register(User, AdminUser)