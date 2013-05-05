from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfile
from connections.admin import ConnectionInInline, ConnectionOutInline
 
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
 
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline,
               ConnectionInInline,
               ConnectionOutInline]
 
admin.site.register(User, UserProfileAdmin)
