import random

from http import HTTPStatus
from django.test import TestCase, Client


# Create your tests here.
class TestUserManagement(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._users = {}
        self._client = Client()

    def test_register_user_successful(self):
        id_ = random.randint(10**5, 10**6)
        res = self.client.post(f'/users/', json={
            'username': f'test-{id_}',
            'password': f'{id_}',
        })

        self.assertEqual(res.status_code, HTTPStatus.CREATED)
