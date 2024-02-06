from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.
#CustomUser instead of default user
 
class CustomUserAdmin(UserAdmin):
    list_display= ('id', 'username', 'email', 'gender')
    search_fields= ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)