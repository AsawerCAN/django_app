from django.contrib import admin
from .models import *

# Register your models here.
#admin
# m.asawernaseer@gmail.com
# OP*(53)yueD2

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'age', 'gender', 'occupation', 'email')
    list_display_links=('name', 'email')
    list_filter= ('gender',)
    search_fields= ('occupation',)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Religion)
admin.site.register(Sect)
admin.site.register(Caste)
admin.site.register(FatherProfile)

class HobbyAdmin(admin.ModelAdmin): #related_name='profiles' add in hobbies sect work by following
    list_display= ('name', 'get_profiles') #get_profile in this case is to display profile list who follow these hobbies
    
    def get_profiles(self, obj):
        hobby_followers= ", ".join([profile.name for profile in obj.profiles.all()]) #",".join function is to seprate profile name with ,"
        return hobby_followers
    
    get_profiles.short_description="Followers"  # to display Followers instead of get_profile  

admin.site.register(Hobbies, HobbyAdmin)