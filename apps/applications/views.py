from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Users can only see their own applications
        return self.queryset.filter(applicant=self.request.user)
    