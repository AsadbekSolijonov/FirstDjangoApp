from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.models import CustomUser, Profile

admin.site.unregister(Group)


class ProfileAdmin(TabularInline):
    model = Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileAdmin, ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("phone",)}),
    )
