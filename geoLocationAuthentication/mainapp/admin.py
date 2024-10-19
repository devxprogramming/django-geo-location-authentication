from django.contrib import admin

from .models import User, UserSession


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'longitude', 'latitude')

admin.site.register(User, UserAdmin)

class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')

admin.site.register(UserSession, UserSessionAdmin)