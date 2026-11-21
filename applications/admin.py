from django.contrib import admin
from .models import CourseApplication


@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "course",
        "phone",
        "status",
        "created_at",
    )

    list_filter = ("status", "course", "created_at")

    search_fields = (
        "full_name",
        "phone",
        "student__username",
        "student__email",
    )

    readonly_fields = ("created_at", "updated_at")