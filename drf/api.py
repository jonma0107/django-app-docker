from .models import Drf
from rest_framework import viewsets, permissions
from .serializers import DrfSerializer
from rest_framework import filters

class DrfViewSet(viewsets.ModelViewSet):
  queryset = Drf.objects.all().order_by('-deliver_date')
  permission_classes = [permissions.AllowAny]
  serializer_class = DrfSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['title', 'state', 'priority', 'deliver_date']

