
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
# from .serializers import TodoSerializer

post_url = 'http://127.0.0.1:8000/todos/todo_create/'

class TodoCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_todo_create(self):
        data = {'title': 'Test Todo', 'completed': True}
        response = self.client.post(post_url, data, format='json')
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['title'], 'Test Todo')
        # Add more assertions based on your serializer and expected data

    def test_todo_create_invalid_data(self):
        data = {'title': '', 'completed': True}
        response = self.client.post(post_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Add more assertions based on your serializer and expected data

    # add the rest of the tests fro CRUD