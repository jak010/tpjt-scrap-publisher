from __future__ import annotations

from django.core.mail import EmailMessage

from apps.models import PublishMemberHistory


class EmailSender:

    def __init__(self,
                 rss,
                 sender,
                 receviers: list[str],
                 content_type="html"
                 ):

        self.rss = rss
        self.sender = sender
        self.receviers = receviers
        self.content_type = content_type

    @property
    def _get_email_message(self) -> EmailMessage:
        return EmailMessage(
            subject="TPJT SCRAP PUBLISH",
            body="<h1>" + self.rss.get_title + "</h1>" + "\n" + self.rss.get_summary,
            to=self.receviers,
        )

    def publish(self, with_history=True):
        email_message = self._get_email_message
        email_message.content_subtype = self.content_type
        result = email_message.send()

        if result != 0 and with_history:

            for receiver in self.receviers:
                publish_history = PublishMemberHistory(
                    sender=self.sender,
                    receiver=receiver,
                    title=self.rss.get_title,
                    content=self.rss.get_summary,
                    description=self.rss.get_summary_detail
                )
                publish_history.save()

        return email_message
