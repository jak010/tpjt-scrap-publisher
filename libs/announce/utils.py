from django.core.mail import EmailMessage
import pickle


def deserialized_email(email_messages: list[bytes]) -> list[EmailMessage]:
    """ seralized -> deserialized """
    objs = []
    for email_message in email_messages:
        deserialize = pickle.loads(email_message)
        objs.append(deserialize)

    return objs
