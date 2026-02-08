from rest_framework import generics
from apps.users.permissions import IsAdmin
from .models import Category
from .serializers import CategorySerializer
from drf_yasg.utils import swagger_auto_schema

# no authentication required for list view
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

    
# authentication required for create view
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
   
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update, or delete a job category by ID. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_summary="Retrieve a category by ID (Admin only)",
        operation_description="Retrieve a specific job category by its ID."
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
   # authentication required for update views
    @swagger_auto_schema(
        operation_summary="Update a category by ID (Admin only)",
        operation_description="Admin authentication required for update view."
        )
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    

    # authentication required for partial update view
    @swagger_auto_schema(
        operation_summary="Partially update a category by ID (Admin only)",
        operation_description="Admin authentication required for partial update view."
        )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
     # authentication required for update and delete views
    @swagger_auto_schema(
        operation_summary="Delete a category by ID (Admin only)",
        operation_description="Admin authentication required for delete view."
        )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)  
