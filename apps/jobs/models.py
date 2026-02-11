from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):        
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=255, unique=True, db_index=True)  # useful if searching by name and fast look up.
    country = models.CharField(max_length=255, db_index=True)  # useful if filtering by country


    def __str__(self):
        return f"{self.city}, {self.country}"
    
    class Meta:
        db_table = "locations_location"

class Job(models.Model):
    title = models.CharField(max_length=255, db_index=True)  # useful if searching by title
    description = models.TextField()
    company = models.CharField(max_length=255)

    # Categorization
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.SET_NULL, null=True, blank=True, db_index=True)  # useful if filtering by category
    location = models.ForeignKey(Location, related_name="jobs", on_delete=models.SET_NULL, null=True, blank=True, db_index=True) # useful if filtering by location
   
    # Job type and experience level

    JOB_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]
    default_job_type = 'CT'  # Default to Contract
    

    EXPERIENCE_LEVEL_CHOICES = [
        ('EN', 'Entry Level'),
        ('MI', 'Mid Level'),
        ('SE', 'Senior Level'),
        ('EX', 'Executive Level'),
    ]
    default_experience_level = 'EN'  # Default to Entry Level

    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default=default_job_type, db_index=True)  # useful if filtering by job type
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES, default=default_experience_level, db_index=True)

    posted_by = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)  # useful if filtering by active jobs
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # useful if sorting by creation date
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} in {self.category} at {self.company}"
    class Meta:
        ordering = ['-created_at',]  
    # Add indexes for commonly queried fields