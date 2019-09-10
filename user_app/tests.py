# -*- coding: utf-8 -*-


from django.test import TestCase
from rest_framework.test import APIRequestFactory

from user_app.models import ApiUser
from webservice.views import login


class TestLogin(TestCase):

    def setUp(self):
        self.user = ApiUser.objects.create_user(username='test', password='test1234')

    def testlogin(self):
        factory = APIRequestFactory()
        request = factory.post('api/login/', {'username':'test', 'password':'test1234'})
        response = login(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['token'])

