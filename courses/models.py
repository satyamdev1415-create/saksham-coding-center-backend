from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    overview = models.TextField( blank=True, default="")
    prerequisites = models.JSONField( default=list, blank=True )
    learning_outcomes = models.JSONField( default=list, blank=True )
    curriculum = models.JSONField( default=list, blank=True )
    projects = models.JSONField( default=list, blank=True )
    faqs = models.JSONField( default=list, blank=True )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title




