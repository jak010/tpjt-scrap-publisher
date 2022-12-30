from __future__ import annotations

from apps.views.publish.dto.email_publish_on_member_dto import EmailPublishOnMemberDto
from libs import constant
from .tistory_rss import TistoryRss, TistoryRssData


def rss_factory(email_publish_on_member_dto: EmailPublishOnMemberDto):
    if email_publish_on_member_dto.get_domain == constant.RSS.TISTORY.value:
        tistory_rss = TistoryRss(sub_domain=email_publish_on_member_dto.get_sub_domain)
        return TistoryRssData(tistory_rss.get_entires_first)
