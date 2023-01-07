from __future__ import annotations

import abc
from typing import List

from feedparser import FeedParserDict


class BaseRss(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    @property
    def get_url(self): ...

    @abc.abstractmethod
    @property
    def _fetch(self) -> FeedParserDict: ...

    @abc.abstractmethod
    @property
    def get_entires(self) -> List[FeedParserDict]: ...

    @abc.abstractmethod
    @property
    def get_entires_first(self): ...
