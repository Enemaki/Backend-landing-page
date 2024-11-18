from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product

class AccountTests(APITestCase):
    def test_create_product(self):
        """
        Ensure we can create a new Product object.
        """
        url = reverse('products')
        data = {'name': 'ps5', 'description': 'An interesting game', 'price': '10.99'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'ps5')
        
    def test_register_user(self):
        """
        Ensure we can register a new user
        """
        url = reverse('register')
        data = {'username': 'eneyems@yahoo.com', 'password': 'musty1234',  'password2': 'musty1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'eneyems@yahoo.com')
        
    def test_login_user(self):
        """
        Ensure we can login a user
        """
        User.objects.create_user(
            username ='eneyems@yahoo.com', password = 'musty1234'
        )
        url = reverse('login')
        data = {'username': 'eneyems@yahoo.com', 'password': 'musty1234'}
        response = self.client.post(url, data, format='json', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, 'eneyems@yahoo.com')