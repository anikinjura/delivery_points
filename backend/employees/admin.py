# backend/employees/admin.py

from django.contrib import admin
from .models import Employee
from .forms import EmployeeForm

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_filter = ['role', 'agent']
    search_fields = ['name']

admin.site.register(Employee, EmployeeAdmin)
