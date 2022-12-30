from __future__ import annotations

from django.core.mail import EmailMessage


# Email Publish
# email_message = EmailMessage(
#     subject=rss.get_title,
#     body=rss.get_summary,
#     to=[email_publish_on_member_dto.get_receiver]
# )
# email_message.content_subtype = "html"
# result = email_message.send()


class EmailSender:

    def __init__(self, subject, body, receviers: list[str], content_type="html"):
        self.subject = subject
        self.body = body
        self.to = receviers
        self.content_type = content_type

    @property
    def get_email_message(self):
        return EmailMessage(
            subject=self.subject,
            body=self.body,
            to=self.to,
        )

    def publish(self):
        email_message = self.get_email_message
        email_message.content_subtype = self.content_type
        email_message.send()
        return email_message