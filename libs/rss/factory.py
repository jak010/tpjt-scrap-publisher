from __future__ import annotations

from .tistory import (
    TistoryRss
)
from .. import constant


def rss_factory(domain: str, sub_domain: str):
    """ domain에 맞는 RSS 데이터 Factory """
    if domain == constant.RSS.TISTORY.value:
        return TistoryRss(sub_domain=sub_domain)
