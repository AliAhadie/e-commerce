from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile
from django.contrib.sessions.models import Session

# تنظیمات مربوط به مدل User

class UserAdmin(BaseUserAdmin):
    list_display = ("email", "is_active", "is_staff", "is_verified", "type")
    list_filter = ("is_active", "is_staff", "is_verified", "type")
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ("last_login", "created_date", "updated_date")

    fieldsets = (
        ("اطلاعات کاربری", {"fields": ("email", "password")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_verified", "is_staff", "groups", "user_permissions")}),
        ("تاریخ‌ها", {"fields": ("last_login", "created_date", "updated_date")}),
    )

    add_fieldsets = (
        ("ایجاد کاربر جدید", {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "type", "is_active", "is_staff"),
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "phone_number")
    search_fields = ("user__email", "first_name", "last_name", "phone_number")
    list_filter = ("created_date",)
    readonly_fields = ("created_date", "updated_date")

admin.site.register(User)
admin.site.register(Profile)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ('session_key', 'expire_date', '_session_data')