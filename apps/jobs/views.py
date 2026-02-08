from rest_framework import generics
from apps.users.permissions import IsAdmin, IsUser
from .models import Job
from .serializers import JobSerializer
from drf_yasg.utils import swagger_auto_schema

# no authentication required for list view
class JobListView(generics.ListCreateAPIView):
    """ List all jobs or create a new job. Supports filtering by category (?category=<id>). """
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer


    @swagger_auto_schema(
        operation_summary="List all jobs User authentication not required", 
        operation_description="Retrieve a list of all job postings."
        )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class JobDetailView(generics.RetrieveAPIView):
    """ Retrieve details of a specific job posting. """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    @swagger_auto_schema(
        operation_summary="Retrieve a job by ID User authentication not required", 
        operation_description="Retrieve details of a specific job posting by its ID."
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class JobCRUDView(generics.CreateAPIView):

    """ Create a new job posting. """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdmin]  # Only admin users can create jobs

    def get_queryset(self):
        # Order jobs by their own created_at field
        return Job.objects.all().order_by('created_at')

    @swagger_auto_schema(
        operation_summary="Create a new job (Admin only)",
        operation_description="Admin authentication required to create a new job posting."
        )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs) 
      
    # authentication required for update views
    @swagger_auto_schema(
        operation_summary="Edit existing jobs (Admin only)",
        operation_description="Admin authentication required to edit existing job postings."
        )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # authentication required for partial update view
    @swagger_auto_schema(
        operation_summary="Partially edit existing jobs (Admin only)",
        operation_description="Admin authentication required to partially edit existing job postings."
        )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)  
    
    # authentication required for delete view
    @swagger_auto_schema(
        operation_summary="Delete existing jobs (Admin only)",
        operation_description="Admin authentication required to delete existing job postings."
        )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

    
