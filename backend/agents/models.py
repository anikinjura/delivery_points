# backend/agents/models.py
from django.db import models
from core.models import ReferenceBook

class Agent(ReferenceBook):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)


    def get_pickup_points(self):
        return self.pickup_points.all()
    
    
    def __str__(self):
        return self.name