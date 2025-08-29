from django.contrib import admin

from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "is_admin", "is_active")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_admin", "is_active")
    ordering = ("email",)
