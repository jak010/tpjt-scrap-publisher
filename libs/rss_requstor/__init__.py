import feedparser
from feedparser import FeedParserDict
from typing import List, Dict


class BaseRss:

    def __init__(self, sub_domain, domain, top_level_domain):
        self._sub_domain = sub_domain
        self._domain = domain
        self._top_level_domain = top_level_domain

    @property
    def get_url(self):
        return "https://" + self._sub_domain + "." + self._domain + "." + self._top_level_domain

    @property
    def _fetch(self) -> FeedParserDict:
        return feedparser.parse(self.get_url + "/rss")

    @property
    def get_entires(self) -> List[FeedParserDict]:
        return self._fetch['entries']
