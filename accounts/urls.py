from django.urls import path
from .views import (
    RegisterAPIView,
    AdminDashboardAPIView,
    AdminStudentListAPIView,
    AdminStudentDetailAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),

    path("admin/dashboard/", AdminDashboardAPIView.as_view()),

    path("admin/students/", AdminStudentListAPIView.as_view()),

    path(
        "admin/students/<int:pk>/",
        AdminStudentDetailAPIView.as_view()
    ),
]