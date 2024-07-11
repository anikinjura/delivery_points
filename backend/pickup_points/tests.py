# backend/pickup_points/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from pickup_points.models import PickupPoint
from agents.models import Agent
from django.urls import reverse

class PickupPointTests(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(
            name='Agent One',
            email='agentone@example.com',
            phone_number='1234567890'
        )
        self.pickup_point_data = {
            'name': 'Pickup Point One',
            'address': '123 Test St',
            'agent': self.agent.id
        }
        self.pickup_point = PickupPoint.objects.create(
            name=self.pickup_point_data['name'],
            address=self.pickup_point_data['address'],
            agent=self.agent
        )

    def test_create_pickup_point(self):
        url = reverse('pickuppoint-list')
        data = {
            'name': 'Pickup Point Two',
            'address': '456 Test Ave',
            'agent': self.agent.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PickupPoint.objects.count(), 2)
        self.assertEqual(PickupPoint.objects.last().name, 'Pickup Point Two')

    def test_get_pickup_points(self):
        url = reverse('pickuppoint-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)  # Проверяем количество объектов
        self.assertEqual(len(response.data['results']), 1)  # Проверяем длину списка объектов

    def test_get_pickup_point(self):
        url = reverse('pickuppoint-detail', args=[self.pickup_point.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.pickup_point.name)

    def test_update_pickup_point(self):
        url = reverse('pickuppoint-detail', args=[self.pickup_point.id])
        updated_data = {
            'name': 'Pickup Point Updated',
            'address': self.pickup_point_data['address'],
            'agent': self.agent.id
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pickup_point.refresh_from_db()
        self.assertEqual(self.pickup_point.name, 'Pickup Point Updated')

    def test_delete_pickup_point(self):
        url = reverse('pickuppoint-detail', args=[self.pickup_point.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PickupPoint.objects.filter(id=self.pickup_point.id).exists())
