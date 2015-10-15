from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from alliance.apps.accounts.factories import UserFactory


class Tests(TestCase):
    def setUp(self):
        super(Tests, self).setUp()
        self.client = Client()

    def test_backlogs(self):
        """
        backlogs endpoint is accessible to any user

        To test: User's only see backlogs they're linked to.
        """
        view = 'backlogs'
        path = reverse(view)

        user = UserFactory()

        self.client.login(username=user.username, password='password')

        response = self.client.get(path)
        # With no team id in my session I get redirected (302)
        self.assertEqual(response.status_code, 302)

        s = self.client.session
        s['team'] = 1
        s.save()

        # With a team id in my session, I should get a normal page load (200)
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)