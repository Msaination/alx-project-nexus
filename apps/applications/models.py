from django.db import models
from apps.jobs.models import Job
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Application(models.Model):
    applicant = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="applications", on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("reviewed", "Reviewed"), ("accepted", "Accepted"), ("rejected", "Rejected")],
        default="pending"
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
    class Meta:
        ordering = ['-applied_at']
