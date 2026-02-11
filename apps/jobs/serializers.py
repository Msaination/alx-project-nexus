from rest_framework import serializers
from .models import Category, Job, Location


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

class LocationSerializer(serializers.ModelSerializer):
    jobs_count = serializers.IntegerField(
        source='jobs.count', 
        read_only=True
    )
    class Meta:
        model = Location
        fields = ['city', 'country', 'jobs_count', 'id']

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    posted_by_username = serializers.CharField(source='posted_by.username', read_only=True) 
    
    class Meta:
        model = Job
        fields = ['title', 'description', 
                  'category_name','company', 
                  'location', 'salary', 'is_active', 
                  'created_at',  'posted_by_username',
                  'id',]