from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Registration
    path("api/auth/", include("accounts.urls")),
    

    # JWT Login
    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    # JWT Refresh
    path(
        "api/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Courses
    path("api/courses/", include("courses.urls")),
    path("api/faculty/", include("faculty.urls")),
    path("api/contact/", include("contact.urls")),

    # Course Applications
    path(
        "api/applications/",
        include("applications.urls"),
    ),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)