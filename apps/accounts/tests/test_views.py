from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import reverse

# Create your tests here.

class AccountsTestCase(APITestCase):
    
    def test_signup(self):
        url = "http://localhost:8000/api/v1/accounts/register"
        data = {'username': "Tundeednut", 'email': "tundeednut@gmail.com", 'password1': 's3r3n1ty', 'password2': 's3r3n1ty', 'first_name': 'Tunde', 'last_name': "Balogun", 'phone_number': '08167467782', 'address': '2, Cole Street Collins Road, Ikeja, Lagos'}
        registerResponse = self.client.post(url, data, format='json')
        print(registerResponse.status_code)

        self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh_token', registerResponse.data)
        self.assertIn('access_token', registerResponse.data)
