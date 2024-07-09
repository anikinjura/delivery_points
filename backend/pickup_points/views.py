# backend/pickup_points/views.py

from rest_framework import viewsets
from .models import PickupPoint
from .serializers import PickupPointSerializer
from dal import autocomplete

class PickupPointViewSet(viewsets.ModelViewSet):
    queryset = PickupPoint.objects.all().order_by('id')  # Add order_by to queryset
    serializer_class = PickupPointSerializer
    filterset_fields = ['agent', 'name']

class PickupPointAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return PickupPoint.objects.none()

        qs = PickupPoint.objects.all().order_by('id')  # Add order_by to queryset

        agent = self.forwarded.get('agent', None)
        if agent:
            qs = qs.filter(agent_id=agent)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
