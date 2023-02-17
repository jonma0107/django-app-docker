from rest_framework import serializers
from .models import Drf

class DrfSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drf
    fields = ('id', 'title', 'description', 'state', 'priority', 'deliver_date', 'comment')


    

