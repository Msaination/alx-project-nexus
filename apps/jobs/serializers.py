from rest_framework import serializers
from .models import Job

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