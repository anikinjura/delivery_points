# backend/employees/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee
from agents.models import Agent
from pickup_points.models import PickupPoint
from django.urls import reverse
from datetime import date

class EmployeeTests(APITestCase):
    def setUp(self):
        # Создание экземпляра Agent
        self.agent = Agent.objects.create(
            name='Agent One',
            email='agentone@example.com',
            phone_number='1234567890'
        )
        # Создание экземпляра PickupPoint
        self.pickup_point = PickupPoint.objects.create(
            name='Pickup Point One',
            address='123 Test St',
            agent=self.agent
        )
        self.employee_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'date_of_birth': '1990-01-01',
            'date_of_hire': date.today(),
            'position': 'Manager',
            'agent': self.agent,  # Присваивание экземпляра Agent
            'default_pickup_point': self.pickup_point, # Присваивание экземпляра PickupPoint
            'role': 'manager',
            'is_active': True
        }
        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        url = reverse('employee-list')
        response = self.client.post(url, self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.employee.first_name)

    def test_update_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        updated_data = self.employee_data.copy()
        updated_data['first_name'] = 'Jane'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Jane')

    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())
