from rest_framework import generics
from rest_framework import serializers

from .models import Departure

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = ('name', 'start_date', 'finish_date', 'category')

class DepartureView(generics.ListAPIView):
    queryset = Departure.objects.all()
    serializer_class = DepartureSerializer
