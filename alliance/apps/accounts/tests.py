from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class Tests(TestCase):
    def setUp(self):
        super(Tests, self).setUp()
        self.client = Client()

    def test_login(self):
        view = 'login'
        path = reverse(view)

        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        """
        Test that the admin site is setup, staff users can go to it,
        non staff users are redirected
        """
        view = 'admin:index'
        path = reverse(view)

        username = 'test user'
        password = 'password'

        user = User(username=username)
        user.set_password(password)
        user.save()

        self.client.login(username=username, password=password)

        response = self.client.get(path)
        self.assertEqual(response.status_code, 302)

        user.is_staff = True
        user.save()

        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)