# backend/agents/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Agent
from django.urls import reverse

class AgentTests(APITestCase):
    def setUp(self):
        self.agent_data = {
            'name': 'Agent One',
            'email': 'agentone@example.com',
            'phone_number': '1234567890',
            'description': 'Test description'
        }
        self.agent = Agent.objects.create(**self.agent_data)

    def test_create_agent(self):
        url = reverse('agent-list')
        response = self.client.post(url, self.agent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_agents(self):
        url = reverse('agent-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.agent.name)

    def test_update_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        updated_data = self.agent_data.copy()
        updated_data['name'] = 'Agent Updated'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agent.refresh_from_db()
        self.assertEqual(self.agent.name, 'Agent Updated')

    def test_delete_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Agent.objects.filter(id=self.agent.id).exists())
