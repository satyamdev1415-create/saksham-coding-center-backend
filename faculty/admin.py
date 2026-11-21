from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "designation",
        "qualification",
        "experience",
        "is_active",
    ]

    list_filter = [
        "is_active",
        "designation",
    ]

    search_fields = [
        "name",
        "designation",
        "qualification",
    ]

    list_editable = [
        "is_active",
    ]

    readonly_fields = [
        "created_at",
    ]