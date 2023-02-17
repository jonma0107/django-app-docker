# from django.urls import path
from rest_framework import routers
from .api import DrfViewSet
# urlpatterns = []

router = routers.DefaultRouter()

router.register('api/drf', DrfViewSet, 'tasks' )

urlpatterns = router.urls


