from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "role", "is_staff", "is_superuser", "is_active"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    list_editable = ["role", "is_active"]