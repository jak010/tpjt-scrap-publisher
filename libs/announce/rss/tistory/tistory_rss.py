from __future__ import annotations

from ..base_rss import BaseRss

import feedparser
from feedparser import FeedParserDict

from typing import List


class TistoryRss(metaclass=BaseRss):

    def __init__(self, sub_domain):
        self._sub_domain = sub_domain
        self._domain = "tistory"
        self._top_level_domain = "com"

    @property
    def get_url(self):
        return "https://" + self._sub_domain + "." + self._domain + "." + self._top_level_domain

    @property
    def _fetch(self) -> FeedParserDict:
        return feedparser.parse(self.get_url + "/rss")

    @property
    def get_entires(self) -> List[FeedParserDict]:
        return self._fetch['entries']

    @property
    def get_entires_first(self):
        return self.get_entires[0]
