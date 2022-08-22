from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    
    fieldsets = UserAdmin.fieldsets + (("Custom profile",
    {"fields": ("avatar", "gender", "bio", "birthday", "language", "currency", "superhost"),}),)

    list_filter = UserAdmin.list_filter + ("superhost",)


    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )