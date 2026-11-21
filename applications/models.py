from django.conf import settings
from django.db import models


class CourseApplication(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONTACTED", "Contacted"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="course_applications",
    )

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.PROTECT,
        related_name="applications",
    )

    full_name = models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,
        default="PENDING",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.course.title}"