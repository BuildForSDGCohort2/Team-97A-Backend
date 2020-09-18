from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import reverse

# Create your tests here.

class AccountsTestCase(APITestCase):
    def signup(self, data):
        url = reverse('accounts:rest_register')
        registerResponse = self.client.post(url, data, format='json')
        print(registerResponse.status_code)

        self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh_token', registerResponse.data)
        self.assertIn('access_token', registerResponse.data)
        return registerResponse

    def test_editDetails(self):
        data = {'username': "Tundeednut", 'email': "tundeednut@gmail.com", 'password1': 's3r3n1ty', 'password2': 's3r3n1ty', 'first_name': 'Tunde', 'last_name': "Balogun", 'phone_number': '08167467782', 'address': '2, Cole Street Collins Road, Ikeja, Lagos'}
        user = self.signup(data).data
        oldData = user
        url = reverse('accounts:users-detail', kwargs={'pk': user['user']['pk']})
        user.update(**{'first_name': 'Olamide', 'last_name': 'Agunbiade', 'email': data['email'], 'phone_number': data['phone_number'], 'address': data['address']})
        response = self.client.put(url, user, HTTP_AUTHORIZATION="Bearer %s" %user['access_token'], format="json")
        print(response.status_code, response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], user['first_name'])
        self.assertEqual(response.data['last_name'], user['last_name'])
