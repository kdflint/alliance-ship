from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from factory import PostGenerationMethodCall


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'test user'
    password = PostGenerationMethodCall('set_password', 'password')
