# backend/employees/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from employees.models import Employee
from agents.models import Agent
from pickup_points.models import PickupPoint

class EmployeeTests(APITestCase):
    def setUp(self):
        # Создание объекта Agent
        self.agent = Agent.objects.create(
            name='Test Agent',
            email='agent@example.com',
            phone_number='1234567890'
        )
        
        # Создание объекта PickupPoint
        self.pickup_point = PickupPoint.objects.create(
            name='Test Pickup Point',
            address='123 Test Address',
            agent=self.agent
        )

        # Данные сотрудника
        self.employee_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '0987654321',
            'date_of_birth': '1990-01-01',
            'date_of_hire': '2020-01-01',
            'position': 'Manager',
            'agent': self.agent,  # Передаем объект Agent
            'default_pickup_point': self.pickup_point,  # Передаем объект PickupPoint
            'is_active': True,
            'name': 'John Doe'  # Добавляем поле name
        }

        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        url = reverse('employee-list')
        new_employee_data = self.employee_data.copy()
        new_employee_data['email'] = 'new.employee@example.com'
        new_employee_data['agent'] = self.agent.id
        new_employee_data['default_pickup_point'] = self.pickup_point.id
        new_employee_data['name'] = 'New Employee Name'

        response = self.client.post(url, new_employee_data, format='json')

        # print(response.data)  # строка для отладки

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_create_employee_invalid(self):
        url = reverse('employee-list')
        invalid_data = self.employee_data.copy()
        invalid_data['email'] = 'invalid-email'
        invalid_data['agent'] = self.agent.id
        invalid_data['default_pickup_point'] = self.pickup_point.id

        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_without_name(self):
        url = reverse('employee-list')
        invalid_data = self.employee_data.copy()
        invalid_data['email'] = 'new.employee@example.com'
        invalid_data['agent'] = self.agent.id
        invalid_data['default_pickup_point'] = self.pickup_point.id
        invalid_data.pop('name')  # Удаляем поле name

        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)


    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_get_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.employee_data['first_name'])

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['first_name'], self.employee_data['first_name'])

    def test_update_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        updated_data = self.employee_data.copy()
        updated_data['first_name'] = 'Jane'
        updated_data['agent'] = self.agent.id
        updated_data['default_pickup_point'] = self.pickup_point.id
        updated_data['name'] = 'Updated Employee Name'

        response = self.client.put(url, updated_data, format='json')

        # print(response.data)  # строка для отладки

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Jane')

    def test_update_employee_invalid(self):
        url = reverse('employee-detail', args=[self.employee.id])
        invalid_data = self.employee_data.copy()
        invalid_data['email'] = 'invalid-email'
        invalid_data['agent'] = self.agent.id
        invalid_data['default_pickup_point'] = self.pickup_point.id

        response = self.client.put(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
