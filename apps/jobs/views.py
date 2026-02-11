from rest_framework import generics
from apps.users.permissions import IsAdmin, IsUser
from .models import Category, Job, Location
from .serializers import JobSerializer, CategorySerializer, LocationSerializer
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse


#Create homepage view
def homepage(request):
    return HttpResponse("Welcome to the Perfect Jobs API! Visit /api/swagger/ for API documentation.")  


# category views
class CategoryListView(generics.ListAPIView):
    """
    List all job categories with counts of active and total jobs.
    Ordered by latest created entry.
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        # Order categories by their own created_at field
        return Category.objects.all().order_by('name')

    @swagger_auto_schema(
        operation_summary="List all categories with job counts, No authentication required", 
        operation_description="Retrieve a list of all job categories along with counts of active and total jobs in each category, ordered by latest created."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class CategoryCreateView(generics.CreateAPIView):
    """ Create a new job category. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_summary="Create a new category (Admin only)",
        operation_description="Admin authentication required for create view."
        )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    # authentication required for update views
    @swagger_auto_schema(
        operation_summary="Edit existing categories (Admin only)",
        operation_description="Admin authentication required to edit existing job categories."
        )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # authentication required for partial update view
    @swagger_auto_schema(
        operation_summary="Partially edit existing categories (Admin only)",
        operation_description="Admin authentication required to partially edit existing job categories."
        )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)  
    
    # authentication required for delete view
    @swagger_auto_schema(
        operation_summary="Delete existing categories (Admin only)",
        operation_description="Admin authentication required to delete existing job categories."
        )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

class CategoryDetailView(generics.RetrieveAPIView):
    """ Retrieve details of a specific job category. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_summary="Retrieve a category by ID User authentication not required",
        operation_description="Retrieve a specific job category by its ID."
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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

class JobCreateView(generics.CreateAPIView):
    """ Create a new job posting. """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdmin]  # Only admin users can create jobs

    @swagger_auto_schema(
        operation_summary="Create a new job (Admin only)",
        operation_description="Admin authentication required to create a new job posting."
        )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class JobEditView(generics.UpdateAPIView):

    """ Update an existing job posting. """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdmin]  # Only admin users can update jobs

    def get_queryset(self):
        # Order jobs by their own created_at field
        return Job.objects.all().order_by('created_at')

    @swagger_auto_schema(
        operation_summary="Edit an existing job (Admin only)",
        operation_description="Admin authentication required to edit an existing job posting."
        )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs) 
    
class JobDeleteView(generics.DestroyAPIView):
    """ Delete an existing job posting. """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdmin]  # Only admin users can delete jobs

    @swagger_auto_schema(
        operation_summary="Delete an existing job (Admin only)",
        operation_description="Admin authentication required to delete an existing job posting."
        )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class LocationListView(generics.ListAPIView):
    """ List all job locations. """
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializer

    @swagger_auto_schema(
        operation_summary="List all locations User authentication not required", 
        operation_description="Retrieve a list of all job locations. List number of jobs for each location ordered by city name."
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)    
      
