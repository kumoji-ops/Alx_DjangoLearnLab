from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


from .models import CustomUser




@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
      fieldsets = DjangoUserAdmin.fieldsets + (
          ('Profile', {'fields': ('bio', 'profile_picture', 'followers') }),
   )
      filter_horizontal = ('groups', 'user_permissions', 'followers')
