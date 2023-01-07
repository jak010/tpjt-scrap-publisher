import unittest

from libs.rss.factory import rss_factory


class TestRssFactory(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_get_tistory_rss_then_true(self):
        tistory_rss = rss_factory(domain="tistory", sub_domain="jakpentest")
        self.assertTrue(tistory_rss.get_all_entry())

    def test_get_tistory_rss_then_fail(self):
        with self.assertRaises(Exception):
            tistory_rss = rss_factory(domain="tistory", sub_domain="")
            self.assertFalse(tistory_rss.get_all_entry())
