# backend/employees/forms.py

from django import forms
from dal import autocomplete
from .models import Employee
from pickup_points.models import PickupPoint


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'default_pickup_point': autocomplete.ModelSelect2(
                url='pickup_point-autocomplete',
                forward=['agent']
            )
        }
