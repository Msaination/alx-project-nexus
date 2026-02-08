from django.urls import path 
from .views import JobDetailView, JobListView, JobCRUDView
urlpatterns = [
    path('', JobListView.as_view(), name='jobs-list'),
    path('details/<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    path('<int:pk>/', JobCRUDView.as_view(), name='jobs-edit'),
   
    
    


]
