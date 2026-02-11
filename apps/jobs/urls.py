from django.urls import path 
from .views import (
    CategoryDetailView,
    CategoryListView,
    CategoryCreateView,
    JobListView,
    JobDetailView,
    JobCreateView,
    JobEditView,
    JobDeleteView,
    LocationListView
)

urlpatterns = [
    # List and create jobs, with optional category filtering (?category=<id>)
    path('', JobListView.as_view(), name='jobs-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    path('create/', JobCreateView.as_view(), name='jobs-create'),
    path('<int:pk>/edit/', JobEditView.as_view(), name='jobs-edit'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='jobs-delete'),




    # path('', JobListView.as_view(), name='jobs-list'),
    # path('details/<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    # path('<int:pk>/', JobCRUDView.as_view(), name='jobs-edit'),
    
    # List and create categories
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories-create'),
    path('<int:pk>/categories/', CategoryDetailView.as_view(), name='categories-detail'),

    path('locations/', LocationListView.as_view(), name='locations-list'),

]

# urlpatterns = [
#     path('', CategoryListView.as_view(), name='categories-list'),
#     path('create/', CategoryCreateView.as_view(), name='categories-create'),
#     path('<int:pk>/', CategoryDetailView.as_view(), name='categories-detail'),
# ]