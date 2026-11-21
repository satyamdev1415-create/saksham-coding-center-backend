from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "subject",
            "message",
            "is_read",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "is_read",
            "created_at",
        ]

        def validate_name(self, value):
            if len(value.strip()) < 2:
                raise serializers.ValidationError(
                    "Name must conatin least 2 Charcter"
                )

            return value.strip()

        def validate_message(self, value):
            if len(value.strip()) < 10:
                raise serializers.ValidationError(
                    "Message must contain at least 10 characters."
                )

            return value.strip()





class AdminContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage

        fields = [
            "id",
            "name",
            "email",
            "phone",
            "subject",
            "message",
            "is_read",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "name",
            "email",
            "phone",
            "subject",
            "message",
            "created_at",
        ]