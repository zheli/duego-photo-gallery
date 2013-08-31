"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

factory = APIRequestFactory()
client = APIClient()

class UserRegisterationTest(TestCase):
    def setUp(self):
        pass
    
    def basicTest(self):
        url = reverse('user-register')
        data = {
                'username':'tester', 
                'first_name':'test', 
                'last_name': 'er',
                'email': 'tester@tester.com',
                'password': '1234'
                }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
