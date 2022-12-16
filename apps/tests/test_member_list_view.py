import unittest
from django.test import Client


class MemberListViewTest(unittest.TestCase):

    def test_member_list_view(self):
        client = Client()

        response = client.get("/api/member/list")

        self.assertEqual(response.status_code, 200)
