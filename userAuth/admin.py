from django.contrib import admin
from . models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'image', 'bio', 'phone', 'verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)