from django.urls import path

from .views import (
    CourseApplicationCreateAPIView,
    MyApplicationsAPIView,
    AdminApplicationListAPIView,
    AdminApplicationDetailAPIView,
)

urlpatterns = [
    
    path(
        "",
        CourseApplicationCreateAPIView.as_view(),
        name="application-create",
    ),

    
    path(
        "my/",
        MyApplicationsAPIView.as_view(),
        name="my-applications",
    ),

    
    path(
        "admin/",
        AdminApplicationListAPIView.as_view(),
        name="admin-applications",
    ),


    path(
        "admin/<int:pk>/",
        AdminApplicationDetailAPIView.as_view(),
        name="admin-application-detail",
    ),
]