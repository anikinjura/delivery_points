# backend/agents/views.py

from rest_framework import viewsets
from .models import Agent
from .serializers import AgentSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all().order_by('id')  # Add order_by to queryset
    serializer_class = AgentSerializer
