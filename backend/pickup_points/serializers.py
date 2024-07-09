# backend/pickup_points/serializers.py
from rest_framework import serializers
from .models import PickupPoint

class PickupPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupPoint
        fields = '__all__'
