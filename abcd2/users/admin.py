from django.contrib import admin
from abcd2.users.models import MNS

# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display        = ("id", "username", "is_staff", "is_superuser")

admin.site.register(MNS, UserAdmin)

