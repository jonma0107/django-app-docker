from .models import Drf
from rest_framework import viewsets, permissions
from .serializers import DrfSerializer

class DrfViewSet(viewsets.ModelViewSet):
  queryset = Drf.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = DrfSerializer


