from apps.core.models import Photo
from apps.rest_api.fields import HIDDEN_PASSWORD_STRING
from django.contrib.auth.models import User
from django.core.files import File as DjangoFile 
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.test import APIRequestFactory, APIClient
import base64
import os

factory = APIRequestFactory()
client = APIClient()
TEST_PATH = os.path.dirname(os.path.abspath(__file__))

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

def get_basic_auth(username):
    credentials = ('%s:password' % username)
    base64_credentials = base64.b64encode(credentials.encode(HTTP_HEADER_ENCODING)).decode(HTTP_HEADER_ENCODING)
    return 'Basic %s' % base64_credentials

class BaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.password = 'password'

        self.main_user = User.objects.create_user(username='main_user', email='main_user@test.com', password=self.password)

class PhotoUploadListAPITest(BaseTestCase):
    def setUp(self):
        super(PhotoUploadListAPITest, self).setUp()
        test_image_filename = os.path.join(TEST_PATH, 'test_images','test_image.jpg')
        with open(test_image_filename) as image_file:
            self.photo_1 = Photo.objects.create(user = self.main_user, title='1', image = DjangoFile(image_file))
            self.photo_2 = Photo.objects.create(user = self.main_user, title='2', image = DjangoFile(image_file))
            self.photo_3 = Photo.objects.create(user = self.main_user, title='3', image = DjangoFile(image_file))

    def test_upload(self):
        url = reverse('photo-upload-list')
        test_image_filename = os.path.join(TEST_PATH, 'test_images','test_image.jpg')
        with open(test_image_filename) as image_file:
            data = {
                    'title': 'test_image',
                    'image': image_file,
                    }
            response = self.client.post(
                    url,
                    data,
                    HTTP_AUTHORIZATION = get_basic_auth(self.main_user),
                    )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data.get('title', None), 'test_image')

    def test_list(self):
        url = reverse('photo-upload-list')
        data = {}
        response = self.client.get(
                url,
                data,
                HTTP_AUTHORIZATION = get_basic_auth(self.main_user),
                )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 3)
