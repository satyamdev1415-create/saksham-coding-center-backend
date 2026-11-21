from django.urls import path

from .views import (
    FacultyListAPIView,
    AdminFacultyListCreateAPIView,
    AdminFacultyDetailAPIView,
)

urlpatterns = [
    
    path(
        "",
        FacultyListAPIView.as_view(),
        name="faculty-list",
    ),

    
    path(
        "admin/",
        AdminFacultyListCreateAPIView.as_view(),
        name="admin-faculty-list-create",
    ),
    

    path(
        "admin/<int:pk>/",
        AdminFacultyDetailAPIView.as_view(),
        name="admin-faculty-detail",
    ),
]