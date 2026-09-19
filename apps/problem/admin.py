from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "is_solved", "created_at")
    search_fields = ["title"]
    list_editable = ["is_solved"]