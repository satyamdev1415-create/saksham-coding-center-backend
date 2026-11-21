from rest_framework import generics
from .models import Faculty
from .serializers import FacultySerializer

from rest_framework.permissions import AllowAny
from courses.permissions import IsAdminUserOnly



class FacultyListAPIView(generics.ListAPIView):
    serializer_class = FacultySerializer
    def get_queryset(self):
        return Faculty.objects.filter(
            is_active=True
        ).order_by("display_order", "id")


class AdminFacultyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FacultySerializer
    permission_classes = [IsAdminUserOnly]


    def get_queryset(self):
        return Faculty.objects.all().order_by(
            "display_order",
            "id"
        )


class AdminFacultyDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = FacultySerializer
    permission_classes = [IsAdminUserOnly]


    def get_queryset(self):
        return Faculty.objects.all()



