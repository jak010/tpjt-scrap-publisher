import unittest
from django.test import Client
from django.shortcuts import reverse

from ..orm import GroupSubScribe


class GroupSubscribeRegisterViewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "author": "jakpentest",
            "sub_domain": "jakpentest",
            "domain": "tistory",
            "top_level_domain": "com"

        }

    def test_group_subscribe_register_view(self):
        client = Client()

        url = reverse("apps:group_subscribe_register", kwargs={"group_id": 2})

        response = client.post(url, data=self.data)

        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls) -> None:
        test_set = GroupSubScribe.objects.get(author="jakpentest")
        test_set.delete()
