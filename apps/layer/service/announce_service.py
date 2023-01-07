from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from libs.announce.email import (
    EmailMessage,
    EmailSender
)
from libs.rss.factory import rss_factory

if TYPE_CHECKING:
    from apps.layer.views.publish.dto.email_publish_on_member_dto import EmailPublishOnMemberDto


class AnnounceEmailService:

    def __init__(self, dto: EmailPublishOnMemberDto):
        self._dto = dto
        self._rss = rss_factory(domain=dto.get_domain)

    def publish(self, sender):
        """ Email Direct Send """
        email_sender = EmailSender(
            email_message=self._get_email_message,
            sender=sender,
            receviers=self._dto.get_receiver,
        )
        return email_sender.publish()

    def publish_with_scheduled(self, sender) -> int:
        """ Email Cached """
        email_sender = EmailSender(
            email_message=self._get_email_message,
            sender=sender,
            receviers=self._dto.get_receiver,
        )

        return email_sender.publish_with_scheduled()

    @cached_property
    def _get_email_message(self) -> EmailMessage:
        return EmailMessage(
            email_subject=self._dto.get_subject,
            email_content_title=self._rss.get_title,
            email_content_body=self._rss.get_summary,
            receviers=self._dto.get_receiver
        )
