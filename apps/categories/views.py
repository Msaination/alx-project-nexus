from django.shortcuts import render


# Create your views here.
# --- IGNORE ---    
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
# --- IGNORE ---

