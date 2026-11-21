from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, AdminStudentSerializer
from courses.permissions import IsAdminUserOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from courses.permissions import IsAdminUserOnly
from courses.models import Course
from faculty.models import Faculty
from applications.models import CourseApplication

from rest_framework.views import APIView
from rest_framework.response import Response




class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]



class AdminDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get(self, request):
        total_courses = Course.objects.count()

        total_faculty = Faculty.objects.count()

        total_applications = CourseApplication.objects.count()

        pending_applications = CourseApplication.objects.filter(
            status="PENDING"
        ).count()

        return Response({
            "message": "Welcome to Saksham Coding Center Admin Dashboard",
            "total_courses": total_courses,
            "total_faculty": total_faculty,
            "total_applications": total_applications,
            "pending_applications": pending_applications,
        })



class AdminStudentListAPIView(generics.ListAPIView):
    serializer_class = AdminStudentSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get_queryset(self):
        return User.objects.filter(
            is_staff=False,
            is_superuser=False
        ).order_by("-date_joined")


class AdminStudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdminStudentSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get_queryset(self):
        return User.objects.filter(
            is_staff=False,
            is_superuser=False
        )










class AdminDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def get(self, request):
        total_courses = Course.objects.count()
        total_faculty = Faculty.objects.count()
        total_applications = CourseApplication.objects.count()

        pending_applications = CourseApplication.objects.filter(
            status="PENDING"
        ).count()

        contacted_applications = CourseApplication.objects.filter(
            status="CONTACTED"
        ).count()

        accepted_applications = CourseApplication.objects.filter(
            status="ACCEPTED"
        ).count()

        rejected_applications = CourseApplication.objects.filter(
            status="REJECTED"
        ).count()

        total_students = request.user.__class__.objects.filter(
            is_staff=False
        ).count()

        recent_applications = CourseApplication.objects.select_related(
            "course"
        ).order_by("-created_at")[:5]

        recent_data = []

        for application in recent_applications:
            recent_data.append({
                "id": application.id,
                "full_name": application.full_name,
                "email": application.email,
                "course_title": application.course.title,
                "status": application.status,
                "created_at": application.created_at,
            })


        return Response({
            "message": "Welcome to Saksham Coding Center Admin Dashboard",
            "total_courses" : total_courses,
            "total_faculty" : total_faculty,
            "total_applications" : total_applications,
            "pending_applications" : pending_applications,
            "total_students" : total_students,

            "application_status": {
                "pending": pending_applications,
                "contacted": contacted_applications,
                "accepted": accepted_applications,
                "rejected": rejected_applications,
            },

            "recent_applications" : recent_data,
        })