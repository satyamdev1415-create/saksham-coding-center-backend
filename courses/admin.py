from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "duration",
        "fee",
        "is_active",
    )

    list_filter = ("is_active",)

    search_fields = ("title", "slug","description")

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = ( "created_at", "updated_at", )

    fieldsets = ( ("Basic Information", { "fields": ( "title", "slug", "description", "duration", "fee", "is_active", ) }), ("Detailed Course Content", { "fields": ( "overview", "prerequisites", "learning_outcomes", "curriculum", "projects", "faqs", ) }), ("Timestamps", { "fields": ( "created_at", "updated_at", ) }), )