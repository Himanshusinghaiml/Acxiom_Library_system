from django.contrib import admin
from .models import User,CreateNewUser
# Register your models here.
class CreateNewUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']  # Customize the fields you want to display in the admin list view

admin.site.register(CreateNewUser, CreateNewUserAdmin)