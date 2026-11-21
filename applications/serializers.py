from rest_framework import serializers

from .models import CourseApplication


class CourseApplicationSerializer(serializers.ModelSerializer):

    course_title = serializers.CharField(
        source="course.title",
        read_only=True
    )

    class Meta:
        model = CourseApplication

        fields = [
            "id",
            "course",
            "course_title",
            "full_name",
            "email",
            "phone",
            "city",
            "qualification",
            "message",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate_course(self, value):
        if not value.is_active:
            raise serializers.ValidationError(
                "This course is currently unavailable."
            )

        return value