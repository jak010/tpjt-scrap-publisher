import unittest
from django.test import Client
from datetime import datetime


class MemberListViewTest(unittest.TestCase):

    def test_member_list_view(self):
        client = Client()

        response = client.get("/api/member/list")

        result = response.json()

        item = result['items'][0]

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(item['member_id'], int)
        self.assertIsInstance(item['email'], str)
        self.assertIsInstance(item['last_login'], str)
        self.assertIsInstance(item['date_of_join'], str)
        self.assertIsInstance(item['is_active'], bool)
