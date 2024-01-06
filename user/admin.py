from .models import Company
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("height", "weight")}),
        (
            _("Permissions"),
            {
                "fields": (
                    # "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "height", "weight", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "height", "weight", "is_staff")
    list_filter = ("is_staff", "is_superuser", "groups")
    search_fields = ("email", "email")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

CustomUser = get_user_model()
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company)