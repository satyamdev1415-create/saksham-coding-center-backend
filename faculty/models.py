from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, help_text="Example : Founder & CEO , HOD - Python , senior java")
    qualification = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to="faculty/",
        blank=True,
        null=True
    )
    bio = models.TextField()
    skills = models.JSONField(default=list, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name