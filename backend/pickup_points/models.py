# backend/pickup_points/models.py
from django.db import models
from agents.models import Agent

class PickupPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, related_name='pickup_points', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
