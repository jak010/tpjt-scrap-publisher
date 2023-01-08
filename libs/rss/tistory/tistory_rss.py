from __future__ import annotations

from typing import List

import feedparser

from .tistory_rss_data import TistoryRssData
from ..base_rss import BaseRss


class TistoryRss(metaclass=BaseRss):

    def __init__(self, sub_domain: str):
        if sub_domain.isspace():
            raise Exception(f"{self.__class__} Sub Domain is Empty")

        self._sub_domain = sub_domain
        self._domain = "tistory"
        self._top_level_domain = "com"

    @property
    def get_url(self):
        return "https://" + self._sub_domain + "." + self._domain + "." + self._top_level_domain

    @property
    def get_feed(self) -> feedparser.FeedParserDict:
        return feedparser.parse(self.get_url + "/rss")

    @property
    def get_entires(self) -> List[feedparser.FeedParserDict]:
        return self.get_feed['entries']

    @property
    def get_entires_first(self) -> TistoryRssData:
        return TistoryRssData(self.get_entires[0])

    def get_all_entry(self) -> List[TistoryRssData]:
        return [
            TistoryRssData(entry) for
            entry in self.get_entires
        ]
