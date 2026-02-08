from django.db import models
from django.conf import settings
from apps.categories.models import Category

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    title = models.CharField(max_length=255, db_index=True)  # useful if searching by title
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.CASCADE, db_index=True)  # useful if filtering by category
    posted_by = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)  # useful if filtering by active jobs
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # useful if sorting by creation date
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at',]  
    # Add indexes for commonly queried fields