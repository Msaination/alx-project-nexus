# apps/jobs/urls.py
from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories-list'),
    path('create/', CategoryCreateView.as_view(), name='categories-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='categories-detail'),
]

