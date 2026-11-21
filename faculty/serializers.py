from rest_framework import serializers
from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = [
            "id",
            "name",
            "designation",
            "qualification",
            "experience",
            "photo",
            "bio",
            "skills",
            "linkedin_url",
            "github_url",
            "email",
            "is_active",
            "display_order",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]