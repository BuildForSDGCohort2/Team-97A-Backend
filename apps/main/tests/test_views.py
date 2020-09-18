from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import reverse
import datetime
from ..import models

# Create your tests here.

class PackageTestCase(APITestCase):
    def createUser(self, data):
        url = reverse('accounts:rest_register')
        registerResponse = self.client.post(url, data, format='json')
        print(registerResponse.data)

        self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh_token', registerResponse.data)
        self.assertIn('access_token', registerResponse.data)
        return registerResponse

    def test_packagecreate(self):
        userData = {'username': "Tundeednut", 'email': "tundeednut@gmail.com", 'password1': 's3r3n1ty', 'password2': 's3r3n1ty', 'first_name': 'Tunde', 'last_name': "Balogun", 'phone_number': '08167467782', 'address': '2, Cole Street Collins Road, Ikeja, Lagos'}
        carrierData = {'username': "d3l1v3r", 'email': "crazyrider@gmail.com", 'password1': 'cr4zyr1d3r', 'password2': 'cr4zyr1d3r', 'first_name': 'Gaius', 'last_name': "Sinclair", 'phone_number': '08144455288', 'address': '3, Kraken Street, Masha Ave, Surulere, Lagos'}
        userID = self.createUser(userData).data['user']['pk']
        carrierID = self.createUser(carrierData).data['user']['pk']
        url = reverse("core:packages-list")
        packageData = {
            'name': 'Hp Pavillion Laptop',
            'weight': 36,
            'category': 'OTHER',
            'price': 10000,
            'pick_location': 'Lagos',
            'dest_location': 'Abuja',
            'delivered_on': str(datetime.datetime.now()+datetime.timedelta(days=2)),
            'description': "Highly fragile package needed to be delivered in perfect condition to the stated address: 2, Sumonu Street, Wuse zone, Abuja",
            'owner': userID,
            'carrier': carrierID
        }
        response = self.client.post(url, packageData, format='json')
        print(response.data, response.status_code)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(models.Package.objects.all()), 1)