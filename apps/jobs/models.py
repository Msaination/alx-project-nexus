from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']  