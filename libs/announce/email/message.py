from __future__ import annotations

from django.core.mail import EmailMessage as _EmailMessage


class EmailMessage:
    def __init__(self,
                 email_subject: str,
                 email_content_title: str,
                 email_content_body: str,
                 receviers: list[str]
                 ):
        self.email_subject = email_subject

        self._email_content_title = email_content_title
        self._email_content_body = email_content_body

        self._receivers = receviers

    @property
    def email_subjecty(self):
        return self.email_subject

    @property
    def content_title(self):
        return "<h1>" + self._email_content_title + "</h1>" + "\n"

    @property
    def content_body(self):
        return self._email_content_body + "\n\n"

    @property
    def receivers(self):
        return self._receivers

    def send(self) -> int:
        email_message = _EmailMessage(
            subject=self.email_subject,
            body=self.content_title + self._email_content_body,
            to=self._receivers
        )
        email_message.content_subtype = "html"

        return email_message.send()
