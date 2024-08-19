# backend/employees/admin.py

from django.contrib import admin
from .models import Employee
from .forms import EmployeeForm

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'position', 'agent', 'is_active')
    list_filter = ['default_pickup_point', 'agent']
    search_fields = ['first_name', 'middle_name', 'last_name', 'email']

admin.site.register(Employee, EmployeeAdmin)
