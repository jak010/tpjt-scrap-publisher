from __future__ import annotations

import abc
from typing import List

from feedparser import FeedParserDict


class BaseRss(abc.ABCMeta):

    @property
    @abc.abstractmethod
    def get_url(self): ...

    @property
    @abc.abstractmethod
    def get_feed(self) -> FeedParserDict: ...

    @property
    @abc.abstractmethod
    def get_entires(self) -> List[FeedParserDict]: ...

    @property
    @abc.abstractmethod
    def get_entires_first(self): ...
