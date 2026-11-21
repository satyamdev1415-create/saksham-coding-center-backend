from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        fields = [ "id", "title", "slug", "description", "duration", "fee", "overview", "prerequisites", "learning_outcomes", "curriculum", "projects", "faqs", "is_active", "created_at", "updated_at", ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
