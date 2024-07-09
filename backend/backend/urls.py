# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agents.views import AgentViewSet
from pickup_points.views import PickupPointViewSet
from employees.views import EmployeeViewSet
from pickup_points.views import PickupPointAutocomplete

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'pickup_points', PickupPointViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('pickup_point-autocomplete/', PickupPointAutocomplete.as_view(), name='pickup_point-autocomplete'),
]
