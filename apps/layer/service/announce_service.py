from __future__ import annotations

from libs.announce.utils import rss_factory

from libs.announce.email_sender import EmailSender

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.layer.views.publish.dto.email_publish_on_member_dto import EmailPublishOnMemberDto


class AnnounceEmailService:

    def __init__(self, dto: EmailPublishOnMemberDto):
        self._dto = dto

        self.rss = rss_factory(
            email_publish_on_member_dto=dto
        )

    def publish(self, sender, with_schedule=False):
        email_sender = EmailSender(
            rss=self.rss,
            subject=self._dto.get_subject,
            sender=sender,
            receviers=self._dto.get_receiver,
        )

        if with_schedule:
            return email_sender.publish_with_scheduled()

        return email_sender.publish()
