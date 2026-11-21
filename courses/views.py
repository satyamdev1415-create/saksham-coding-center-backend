from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAdminOrReadOnly

class CourseListAPIView(generics.ListCreateAPIView):


    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Course.objects.all()

        return Course.objects.filter(is_active=True)


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Course.objects.all()

        return Course.objects.filter(is_active=True)




