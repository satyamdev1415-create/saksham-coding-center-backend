from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import CourseApplication
from .serializers import CourseApplicationSerializer
from courses.permissions import IsAdminUserOnly


class CourseApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseApplicationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(student=self.request.user)
        else:
            serializer.save(student=None)


class MyApplicationsAPIView(generics.ListAPIView):
    serializer_class = CourseApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseApplication.objects.filter(
            student=self.request.user
        ).select_related("course")


# Admin: View all applications
class AdminApplicationListAPIView(generics.ListAPIView):
    serializer_class = CourseApplicationSerializer
    permission_classes = [IsAdminUserOnly]

    def get_queryset(self):
        return CourseApplication.objects.all().select_related(
            "course",
            "student"
        )


# Admin: Update application status
class AdminApplicationDetailAPIView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = CourseApplicationSerializer
    permission_classes = [IsAdminUserOnly]

    def get_queryset(self):
        return CourseApplication.objects.all().select_related(
            "course",
            "student"
        )