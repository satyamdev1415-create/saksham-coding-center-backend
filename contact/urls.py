from django.urls import path

from .views import (
    ContactMessageCreateAPIView,
    AdminContactMessageListAPIView,
    AdminContactMessageDetailAPIView,
)


urlpatterns = [
    path(
        "",
        ContactMessageCreateAPIView.as_view(),
        name="contact-create",
    ),

    path(
        "admin/",
        AdminContactMessageListAPIView.as_view(),
        name="admin-contact-list",
    ),

    path(
        "admin/<int:pk>/",
        AdminContactMessageDetailAPIView.as_view(),
        name="admin-contact-detail",
    ),
]