from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserAccount

# User Account Admin
class UserAccountAdmin(BaseUserAdmin):
    list_display = ("email", "full_name", "date_joined", "last_login", "is_admin", "is_staff",)
    search_fields = ("email", "full_name",)
    readonly_fields = ("id", "date_joined", "last_login",)
    ordering = ("email",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(UserAccount, UserAccountAdmin)