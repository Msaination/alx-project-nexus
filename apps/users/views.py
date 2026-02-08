from django.contrib.auth import get_user_model
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer
from .permissions import IsAdmin  # 👈 custom permission you defined

User = get_user_model()


class UserListView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be listed or created.
    Restricted to users with role == ADMIN.
    Supports filtering by ?username=<value>.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        queryset = User.objects.all().order_by('username')  # alphabetical ascending
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset

    @swagger_auto_schema(
        operation_summary="List all users (Admin only)",
        operation_description="Admin role required. Supports filtering by ?username=<value>."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new user (Admin only)",
        operation_description="Admin role required to create a new user."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a user to be retrieved, updated, or deleted.
    Restricted to users with role == ADMIN.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_summary="Retrieve a user by ID",
        operation_description="Admin role required."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a user by ID",
        operation_description="Admin role required."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a user by ID",
        operation_description="Admin role required."
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
