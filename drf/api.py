import django_filters.rest_framework
from .models import Drf
from rest_framework import viewsets, permissions
from .serializers import DrfSerializer
from rest_framework import filters

class DrfViewSet(viewsets.ModelViewSet):
  queryset = Drf.objects.all().order_by('-deliver_date')
  permission_classes = [permissions.AllowAny]
  serializer_class = DrfSerializer
  # filter_backends = [filters.SearchFilter]
  filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['title', 'state', 'priority', 'deliver_date']
  ordering_fields = ['deliver_date']

