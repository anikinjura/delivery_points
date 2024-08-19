# backend/pickup_points/models.py
from django.db import models
from agents.models import Agent
from core.models import ReferenceBook

class PickupPoint(ReferenceBook):
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, related_name='pickup_points', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
