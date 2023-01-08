import unittest
from django.test import Client
from django.shortcuts import reverse

from django.contrib.auth import get_user_model

Member = get_user_model()


class TestEmailPublishOnMemberView(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "receiver": "bluetoon@naver.com",
            "subject": "TEST EMAIL",
            "sub_domain": "jakpentest",
            "domain": "tistory",
            "top_level_domain": "com"
        }

    def test_group_subscribe_register_view(self):
        m = Member.objects.get(email="test01@test.com")

        client = Client()
        client.force_login(m)

        url = reverse("apps:publish_email_on_member")

        response = client.post(url, data=self.data)

        self.assertEqual(response.status_code, 201)
