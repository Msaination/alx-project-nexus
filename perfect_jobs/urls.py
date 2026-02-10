from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.jobs.views import homepage  # Import the homepage view

schema_view = get_schema_view(
    openapi.Info(
        title="Perfect Jobs API",
        default_version='v1',
        description="API documentation for Perfect Jobs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#page for app urls
urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/categories/', include('apps.categories.urls'), name='categories'),
    path('api/jobs/', include('apps.jobs.urls'), name='jobs'),
    path('api/applications/', include('apps.applications.urls'),),
    
    path('api/auth/', include('apps.auth.urls'), name='auth'),
    path('api/', include('apps.users.urls'), name='users'),

    
]
