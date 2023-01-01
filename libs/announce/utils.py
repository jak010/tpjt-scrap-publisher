from __future__ import annotations

import pickle
from typing import TYPE_CHECKING

from django.core.mail import EmailMessage

from .rss.tistory_rss import TistoryRss, TistoryRssData
from .. import constant

if TYPE_CHECKING:
    from apps.views.publish.dto.email_publish_on_member_dto import EmailPublishOnMemberDto


def deserialized_email(email_messages: list[bytes]) -> list[EmailMessage]:
    """ seralized -> deserialized """

    return [pickle.loads(email_message) for
            email_message in email_messages]


def rss_factory(email_publish_on_member_dto: EmailPublishOnMemberDto):
    """ domain 에 맞는 RSS 데이터 Factory """
    if email_publish_on_member_dto.get_domain == constant.RSS.TISTORY.value:
        tistory_rss = TistoryRss(sub_domain=email_publish_on_member_dto.get_sub_domain)
        return TistoryRssData(tistory_rss.get_entires_first)
