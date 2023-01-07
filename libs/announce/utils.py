from __future__ import annotations

import pickle

from django.core.mail import EmailMessage


def deserialized_email(email_messages: list[bytes]) -> list[EmailMessage]:
    """ seralized -> deserialized """

    return [pickle.loads(email_message) for
            email_message in email_messages]
