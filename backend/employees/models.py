# backend/employees/models.py

from django.db import models
from agents.models import Agent
from pickup_points.models import PickupPoint

class Employee(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('accountant', 'Accountant'),
        ('delivery_staff', 'Delivery Staff'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_hire = models.DateField()
    position = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    default_pickup_point = models.ForeignKey(PickupPoint, on_delete=models.SET_NULL, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='other')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
