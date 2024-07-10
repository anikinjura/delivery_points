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
        new_agent_data = {
            'name': 'Agent Two',
            'email': 'agenttwo@example.com',
            'phone_number': '0987654321',
            'description': 'Another test description'
        }
        response = self.client.post(url, new_agent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.count(), 2)

    def test_create_agent_invalid(self):
        url = reverse('agent-list')
        invalid_data = self.agent_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_agents(self):
        # Выполнить запрос GET к endpoint 'agent-list'
        url = reverse('agent-list')
        response = self.client.get(url, format='json')

        # Печатаем содержимое response.data для отладки
        # print(response.data)

        # Проверяем, что статус код ответа равен HTTP_200_OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе есть ровно один агент
        self.assertEqual(response.data['count'], 1)

    def test_get_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.agent.name)

    def test_get_agent_not_found(self):
        url = reverse('agent-detail', args=[999])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        updated_data = self.agent_data.copy()
        updated_data['name'] = 'Agent Updated'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agent.refresh_from_db()
        self.assertEqual(self.agent.name, 'Agent Updated')

    def test_update_agent_invalid(self):
        url = reverse('agent-detail', args=[self.agent.id])
        invalid_data = self.agent_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.put(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_agent(self):
        url = reverse('agent-detail', args=[self.agent.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Agent.objects.filter(id=self.agent.id).exists())

    def test_delete_agent_not_found(self):
        url = reverse('agent-detail', args=[999])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
