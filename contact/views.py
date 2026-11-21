from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import ContactMessage
from .serializers import (
    ContactMessageSerializer,
    AdminContactMessageSerializer,
)
from courses.permissions import IsAdminUserOnly


class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]


class AdminContactMessageListAPIView(generics.ListAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = AdminContactMessageSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOnly]


class AdminContactMessageDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = ContactMessage.objects.all()
    serializer_class = AdminContactMessageSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

