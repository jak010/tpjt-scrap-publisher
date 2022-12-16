import unittest

from functools import cached_property

from django.test import Client
from django.shortcuts import reverse
from ..orm import Member


class MemberCreateViewTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.member_create_data = {
            "email": "test01@test.com",
            "password": "1234"
        }
        return cls

    @cached_property
    def test_client(self) -> Client:
        return Client()

    def test_member_create_view(self):
        response = self.test_client.post(
            "/api/member",
            data=self.member_create_data
        )

        self.assertEqual(response.status_code, 201)

    def test_member_duplicate(self):
        response = self.test_client.post(
            "/api/member",
            data=self.member_create_data
        )

        self.assertEqual(response.status_code, 400)

    @classmethod
    def tearDownClass(cls) -> None:
        member = Member.objects.get(
            email=cls.member_create_data['email']
        )
        member.delete()
