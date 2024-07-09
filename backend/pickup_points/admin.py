# backend/pickup_points/admin.py
from django.contrib import admin
from .models import PickupPoint

class PickupPointAdmin(admin.ModelAdmin):
    list_filter = ('agent',)
    search_fields = ('name',)

admin.site.register(PickupPoint, PickupPointAdmin)
