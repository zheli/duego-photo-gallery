from apps.rest_api.fields import HIDDEN_PASSWORD_STRING
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

factory = APIRequestFactory()
client = APIClient()

class UserRegisterationAPITest(TestCase):
    def test_basic_function(self):
        url = reverse('user-register')
        data = {
                'username':'tester', 
                'first_name':'test', 
                'last_name': 'er',
                'email': 'tester@tester.com',
                'password': '1234'
                }
        expected_result = dict(data)
        expected_result['id'] = 1
        expected_result['password'] = HIDDEN_PASSWORD_STRING
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_result)

def get_basic_auth(username, password):
    credentials = ('%s:password' % username)
    base64_credentials = base64.b64encode(credentials.encode(HTTP_HEADER_ENCODING)).decode(HTTP_HEADER_ENCODING)
    return 'Basic %s' % base64_credentials

class BaseTestCase(TestCase):
    def setUp(self):
        self.client =APIClient(enforce_csrf_checks=True)
        self.password = 'password'

        self.main_user = User.objects.create_user(username='main_user', email='main_user@test.com', password=self.password)

class PhotoUploadListAPITest(TestCase)
