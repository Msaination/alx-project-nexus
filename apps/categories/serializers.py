from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    active_jobs_count = serializers.IntegerField(
        source='jobs.filter(is_active=True).count', 
        read_only=True    
    )
    
    total_jobs_count = serializers.IntegerField(
        source='jobs.count', 
        read_only=True
    )
    
    class Meta:
        model = Category
        fields = ['name', 'description', 'active_jobs_count', 'total_jobs_count', 'id']

